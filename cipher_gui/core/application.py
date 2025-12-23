"""
Main Application Class
======================
Core application window and logic for the Classical Cipher Tool GUI.

This module contains the main CipherGUI class which orchestrates
all UI components, cipher operations, and user interactions.

Classes:
    CipherGUI: Main application window (QMainWindow subclass)

Author: Cipher Tool Team
"""

import os
import sys
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                              QApplication, QMessageBox, QTabWidget, QTabBar)
from PyQt6.QtGui import QAction, QKeySequence, QFont
from PyQt6.QtCore import QSize

from ciphers.caesar_cipher import CaesarCipher
from ciphers.affine_cipher import AffineCipher
from ciphers.playfair_cipher import PlayfairCipher
from ciphers.hill_cipher import HillCipher

from cipher_gui.models.history import HistoryManager
from cipher_gui.models.cipher_config import CipherConfig
from cipher_gui.core.settings import SettingsManager
from cipher_gui.ui.theme import Theme
from cipher_gui.ui.header import HeaderWidget
from cipher_gui.ui.left_panel import LeftPanel
from cipher_gui.ui.right_panel import RightPanel
from cipher_gui.dialogs.about_dialog import AboutDialog
from cipher_gui.dialogs.history_dialog import HistoryDialog
from cipher_gui.actions.cipher_actions import CipherActions
from cipher_gui.actions.file_actions import FileActions
from cipher_gui.actions.ui_actions import UIActions
from cipher_gui.utils.validators import validate_key
from cipher_gui.widgets.cracker_panel import CrackerPanel


class CipherGUI(QMainWindow):
    """
    Main application window for the Classical Cipher Tool.
    
    Provides a tabbed interface with:
    - Cipher tab: Encrypt/decrypt with 4 classical ciphers
    - Crack tab: Hill cipher known plaintext attack
    
    Args:
        crack_mode (bool): If True, opens directly to the Crack tab
    
    Attributes:
        cipher_map (dict): Maps cipher names to cipher instances
        history_manager: Manages operation history
        settings_manager: Handles persistent settings
    """
    
    def __init__(self, crack_mode=False):
        super().__init__()
        self.crack_mode = crack_mode
        
        # Initialize cipher instances
        self.cipher_map = {
            "Caesar": CaesarCipher(),
            "Affine": AffineCipher(),
            "Playfair": PlayfairCipher(),
            "Hill (2×2)": HillCipher()
        }
        
        # Initialize managers
        self.history_manager = HistoryManager()
        self.settings_manager = SettingsManager()
        self.config = CipherConfig
        
        # Initialize action handlers
        self.cipher_actions = CipherActions(self)
        self.file_actions = FileActions(self)
        self.ui_actions = UIActions(self)
        
        self.init_ui()
        self.restore_settings()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Classical Cipher Tool")
        self.setGeometry(100, 100, 1500, 920)
        self.setMinimumSize(1200, 750)
        
        # Create menu bar and toolbar
        self.create_menu_bar()
        self.create_toolbar()
        
        # Central widget with tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        self.header = HeaderWidget()
        main_layout.addWidget(self.header)
        
        # Tab widget for Cipher/Crack modes
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background-color: #0d1117;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background-color: #161b22;
                color: #8b949e;
                border: none;
                padding: 10px 32px;
                margin: 0 1px;
                font-size: 12px;
                font-weight: 500;
            }
            QTabBar::tab:selected {
                background-color: #21262d;
                color: #c9d1d9;
                border-bottom: 2px solid #58a6ff;
            }
            QTabBar::tab:hover:!selected {
                background-color: #1c2128;
                color: #c9d1d9;
            }
        """)
        
        # Cipher tab (main functionality)
        cipher_tab = QWidget()
        cipher_layout = QHBoxLayout(cipher_tab)
        cipher_layout.setContentsMargins(20, 20, 20, 20)
        cipher_layout.setSpacing(20)
        
        # Left panel
        self.left_panel = LeftPanel()
        self.left_panel.action_requested.connect(self.perform_action)
        self.left_panel.validate_requested.connect(self.validate_action)
        self.left_panel.clear_requested.connect(self.clear_action)
        self.left_panel.swap_requested.connect(self.swap_texts)
        self.left_panel.mode_changed.connect(self.on_mode_changed)
        self.left_panel.input_section.import_requested.connect(self.import_text)
        self.left_panel.output_section.copy_requested.connect(self.copy_output)
        self.left_panel.output_section.export_requested.connect(self.export_result)
        self.left_panel.key_section.key_changed.connect(self.on_key_changed)
        cipher_layout.addWidget(self.left_panel, 3)
        
        # Right panel with cipher selector
        self.right_panel = RightPanel(
            self.config.get_all_cipher_names(),
            self.config.CIPHER_ICONS
        )
        self.right_panel.cipher_changed.connect(self.on_cipher_changed)
        cipher_layout.addWidget(self.right_panel, 2)
        
        self.tab_widget.addTab(cipher_tab, "Cipher")
        
        # Cracker tab
        self.cracker_panel = CrackerPanel()
        self.cracker_panel.status_message.connect(self.statusBar().showMessage)
        self.tab_widget.addTab(self.cracker_panel, "Crack")
        
        main_layout.addWidget(self.tab_widget, 1)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Apply theme
        self.setStyleSheet(Theme.get_stylesheet())
        
        # Update initial info
        self.update_cipher_info()
        
        # Switch to crack tab if --crack flag was used
        if self.crack_mode:
            self.tab_widget.setCurrentIndex(1)
    
    def create_menu_bar(self):
        """Create the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        import_action = QAction("📥 Import Text...", self)
        import_action.setShortcut(QKeySequence("Ctrl+O"))
        import_action.triggered.connect(self.import_text)
        file_menu.addAction(import_action)
        
        export_action = QAction("📤 Export Result...", self)
        export_action.setShortcut(QKeySequence("Ctrl+S"))
        export_action.triggered.connect(self.export_result)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("🚪 Exit", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        
        clear_action = QAction("🧹 Clear All", self)
        clear_action.setShortcut(QKeySequence("Ctrl+L"))
        clear_action.triggered.connect(self.clear_action)
        edit_menu.addAction(clear_action)
        
        swap_action = QAction("🔄 Swap Input/Output", self)
        swap_action.setShortcut(QKeySequence("Ctrl+W"))
        swap_action.triggered.connect(self.swap_texts)
        edit_menu.addAction(swap_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        
        history_action = QAction("📜 View History", self)
        history_action.setShortcut(QKeySequence("Ctrl+H"))
        history_action.triggered.connect(self.show_history)
        view_menu.addAction(history_action)
        
        view_menu.addSeparator()
        
        cipher_tab_action = QAction("Cipher Tab", self)
        cipher_tab_action.setShortcut(QKeySequence("Ctrl+1"))
        cipher_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(0))
        view_menu.addAction(cipher_tab_action)
        
        crack_tab_action = QAction("Crack Tab", self)
        crack_tab_action.setShortcut(QKeySequence("Ctrl+2"))
        crack_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))
        view_menu.addAction(crack_tab_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("ℹ️ About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        guide_action = QAction("📖 Quick Guide", self)
        guide_action.setShortcut(QKeySequence("F1"))
        guide_action.triggered.connect(self.ui_actions.show_guide)
        help_menu.addAction(guide_action)
    
    def create_toolbar(self):
        """Create the toolbar."""
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(24, 24))
        
        encrypt_btn = QAction("🔒 Encrypt", self)
        encrypt_btn.triggered.connect(lambda: self.left_panel._set_mode("encrypt"))
        toolbar.addAction(encrypt_btn)
        
        decrypt_btn = QAction("🔓 Decrypt", self)
        decrypt_btn.triggered.connect(lambda: self.left_panel._set_mode("decrypt"))
        toolbar.addAction(decrypt_btn)
        
        toolbar.addSeparator()
        
        validate_btn = QAction("✓ Validate", self)
        validate_btn.triggered.connect(self.validate_action)
        toolbar.addAction(validate_btn)
        
        clear_btn = QAction("🧹 Clear", self)
        clear_btn.triggered.connect(self.clear_action)
        toolbar.addAction(clear_btn)
        
        toolbar.addSeparator()
        
        history_btn = QAction("📜 History", self)
        history_btn.triggered.connect(self.show_history)
        toolbar.addAction(history_btn)
        
        toolbar.addSeparator()
        
        crack_btn = QAction("Crack Hill", self)
        crack_btn.setToolTip("Switch to Hill Cipher Cracker (Ctrl+2)")
        crack_btn.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))
        toolbar.addAction(crack_btn)
    
    def on_cipher_changed(self, cipher_name):
        """Handle cipher selection change."""
        self.update_key_help()
        self.update_cipher_info()
        self.validate_key_silent()
        
        self.statusBar().showMessage(f"Cipher changed to {cipher_name}")
    
    def on_key_changed(self):
        """Handle key input change."""
        self.validate_key_silent()
    
    def on_mode_changed(self, mode):
        """Handle mode change."""
        self.statusBar().showMessage(f"Mode: {mode.capitalize()}")
    
    def get_current_cipher(self):
        """Get current cipher instance."""
        cipher_name = self.right_panel.cipher_selector.get_current_cipher()
        return self.cipher_map[cipher_name], cipher_name
    
    def update_key_help(self):
        """Update key help text."""
        cipher_name = self.right_panel.cipher_selector.get_current_cipher()
        help_data = self.config.get_key_help(cipher_name)
        self.left_panel.key_section.set_key_help(help_data)
    
    def update_cipher_info(self):
        """Update cipher information display."""
        cipher_name = self.right_panel.cipher_selector.get_current_cipher()
        info = self.config.get_cipher_info(cipher_name)
        self.right_panel.info_card.update_info(info)
    
    def validate_key_silent(self):
        """Silently validate key and show indicator."""
        key_text = self.left_panel.key_section.get_key()
        
        if not key_text:
            self.left_panel.key_section.set_validation(False, "")
            return
        
        cipher, _ = self.get_current_cipher()
        is_valid, message = validate_key(cipher, key_text)
        self.left_panel.key_section.set_validation(is_valid, message)
    
    def perform_action(self):
        """Perform encrypt or decrypt action."""
        mode = self.left_panel.get_mode()
        cipher, cipher_name = self.get_current_cipher()
        
        input_text = self.left_panel.input_section.get_text()
        key_text = self.left_panel.key_section.get_key()
        
        if mode == "encrypt":
            result = self.cipher_actions.encrypt(cipher, input_text, key_text)
        else:
            result = self.cipher_actions.decrypt(cipher, input_text, key_text)
        
        if result:
            self.left_panel.output_section.set_text(result)
            self.statusBar().showMessage(
                f"✓ {mode.capitalize()}ed successfully! ({len(result)} characters)", 
                3000
            )
            
            # Add to history
            if self.left_panel.options_section.should_save_history():
                self.history_manager.add_entry(
                    cipher_name, mode, input_text, key_text, result
                )
            
            # Flash success
            self.left_panel.output_section.flash_success()
    
    def validate_action(self):
        """Validate the key."""
        cipher, cipher_name = self.get_current_cipher()
        key_text = self.left_panel.key_section.get_key()
        help_data = self.config.get_key_help(cipher_name)
        
        if self.ui_actions.validate_key_dialog(
            cipher, cipher_name, key_text, help_data['details']
        ):
            self.statusBar().showMessage("✓ Key is valid", 3000)
    
    def clear_action(self):
        """Clear all fields."""
        if self.ui_actions.clear_all(
            self.left_panel.input_section,
            self.left_panel.key_section,
            self.left_panel.output_section
        ):
            self.statusBar().showMessage("✓ All fields cleared", 2000)
    
    def swap_texts(self):
        """Swap input and output texts."""
        if self.ui_actions.swap_texts(
            self.left_panel.input_section,
            self.left_panel.output_section
        ):
            self.statusBar().showMessage("✓ Texts swapped", 2000)
        else:
            self.statusBar().showMessage("Nothing to swap", 2000)
    
    def copy_output(self):
        """Copy output to clipboard."""
        output = self.left_panel.output_section.get_text()
        if self.ui_actions.copy_to_clipboard(output):
            self.statusBar().showMessage("✓ Copied to clipboard", 2000)
            self.left_panel.output_section.flash_success()
        else:
            self.statusBar().showMessage("Nothing to copy", 2000)
    
    def import_text(self):
        """Import text from file."""
        text, filename = self.file_actions.import_text()
        if text:
            self.left_panel.input_section.set_text(text)
            self.statusBar().showMessage(
                f"✓ Imported {len(text)} characters from {os.path.basename(filename)}", 
                3000
            )
    
    def export_result(self):
        """Export result to file."""
        output = self.left_panel.output_section.get_text()
        success, filename = self.file_actions.export_text(output)
        if success:
            self.statusBar().showMessage(
                f"✓ Exported to {os.path.basename(filename)}", 
                3000
            )
    
    def show_history(self):
        """Show history dialog."""
        dialog = HistoryDialog(self.history_manager, self)
        dialog.exec()
    
    def show_about(self):
        """Show about dialog."""
        dialog = AboutDialog(self)
        dialog.exec()
    
    def save_settings(self):
        """Save application settings."""
        self.settings_manager.save_window_geometry(self.saveGeometry())
        self.settings_manager.save_cipher_index(self.header.get_current_index())
        self.settings_manager.save_mode(self.left_panel.get_mode())
        self.settings_manager.save_preserve_case(
            self.left_panel.options_section.should_preserve_case()
        )
        self.settings_manager.save_auto_history(
            self.left_panel.options_section.should_save_history()
        )
    
    def restore_settings(self):
        """Restore application settings."""
        geometry = self.settings_manager.restore_window_geometry()
        if geometry:
            self.restoreGeometry(geometry)
        
        cipher_index = self.settings_manager.restore_cipher_index()
        cipher_names = self.config.get_all_cipher_names()
        if 0 <= cipher_index < len(cipher_names):
            self.right_panel.cipher_selector.set_current_cipher(cipher_names[cipher_index])
        
        mode = self.settings_manager.restore_mode()
        self.left_panel._set_mode(mode)
        
        preserve_case = self.settings_manager.restore_preserve_case()
        self.left_panel.options_section.set_preserve_case(preserve_case)
        
        auto_history = self.settings_manager.restore_auto_history()
        self.left_panel.options_section.set_auto_history(auto_history)
    
    def closeEvent(self, event):
        """Handle window close event."""
        self.save_settings()
        event.accept()
