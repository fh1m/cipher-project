"""Left panel with input/output sections."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import pyqtSignal
from cipher_gui.widgets.modern_button import ModernButton
from cipher_gui.widgets.input_section import InputSection
from cipher_gui.widgets.key_section import KeySection
from cipher_gui.widgets.options_section import OptionsSection
from cipher_gui.widgets.output_section import OutputSection


class LeftPanel(QFrame):
    """Left panel containing mode selector and I/O sections."""
    
    mode_changed = pyqtSignal(str)
    action_requested = pyqtSignal()
    validate_requested = pyqtSignal()
    clear_requested = pyqtSignal()
    swap_requested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("panel")
        self.current_mode = "encrypt"
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Mode selector - CHIP STYLE
        mode_container = QFrame()
        mode_container.setObjectName("modeContainer")
        mode_layout = QHBoxLayout(mode_container)
        mode_layout.setContentsMargins(6, 6, 6, 6)
        mode_layout.setSpacing(6)
        
        mode_label = QLabel("Mode:")
        mode_label.setStyleSheet("font-size: 11px; font-weight: 500; color: #7d8590;")
        mode_layout.addWidget(mode_label)
        
        self.encrypt_mode_btn = ModernButton("Encrypt", "#3fb950")
        self.encrypt_mode_btn.clicked.connect(lambda: self._set_mode("encrypt"))
        self.encrypt_mode_btn.setCheckable(True)
        mode_layout.addWidget(self.encrypt_mode_btn, 1)
        
        self.decrypt_mode_btn = ModernButton("Decrypt", "#f0883e")
        self.decrypt_mode_btn.clicked.connect(lambda: self._set_mode("decrypt"))
        self.decrypt_mode_btn.setCheckable(True)
        mode_layout.addWidget(self.decrypt_mode_btn, 1)
        
        layout.addWidget(mode_container)
        
        # Input section (flexible height)
        self.input_section = InputSection()
        layout.addWidget(self.input_section, 3)  # Takes 3/10 of space
        
        # Key section (compact)
        self.key_section = KeySection()
        layout.addWidget(self.key_section, 1)  # Takes 1/10 of space
        
        # Options section (compact)
        self.options_section = OptionsSection()
        layout.addWidget(self.options_section, 0)  # Fixed size
        
        # Action button - slimmer
        self.action_btn = ModernButton("Encrypt Now", "#3fb950")
        self.action_btn.setMinimumHeight(32)
        self.action_btn.setMaximumHeight(32)
        self.action_btn.clicked.connect(self.action_requested.emit)
        self.action_btn.setStyleSheet("""
            QPushButton {
                background-color: #3fb950;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 0px 20px;
                font-size: 12px;
                font-weight: 600;
                min-height: 32px;
                max-height: 32px;
            }
            QPushButton:hover {
                background-color: #56d364;
            }
            QPushButton:pressed {
                background-color: #2ea043;
            }
        """)
        layout.addWidget(self.action_btn)
        
        # Quick actions - slimmer chips
        quick_actions = QHBoxLayout()
        quick_actions.setSpacing(6)
        
        validate_btn = QPushButton("Validate")
        validate_btn.setMaximumHeight(26)
        validate_btn.clicked.connect(self.validate_requested.emit)
        validate_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #58a6ff;
                border: 1px solid rgba(88, 166, 255, 0.3);
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                max-height: 26px;
            }
            QPushButton:hover {
                background-color: rgba(88, 166, 255, 0.12);
                border-color: #58a6ff;
            }
        """)
        quick_actions.addWidget(validate_btn)
        
        clear_btn = QPushButton("Clear")
        clear_btn.setMaximumHeight(26)
        clear_btn.clicked.connect(self.clear_requested.emit)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7d8590;
                border: 1px solid rgba(125, 133, 144, 0.3);
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                max-height: 26px;
            }
            QPushButton:hover {
                background-color: rgba(125, 133, 144, 0.12);
                border-color: #7d8590;
            }
        """)
        quick_actions.addWidget(clear_btn)
        
        swap_btn = QPushButton("Swap")
        swap_btn.setMaximumHeight(26)
        swap_btn.clicked.connect(self.swap_requested.emit)
        swap_btn.setToolTip("Swap input and output (Ctrl+W)")
        swap_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #bc8cff;
                border: 1px solid rgba(188, 140, 255, 0.3);
                border-radius: 4px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: 500;
                max-height: 26px;
            }
            QPushButton:hover {
                background-color: rgba(188, 140, 255, 0.12);
                border-color: #bc8cff;
            }
        """)
        quick_actions.addWidget(swap_btn)
        
        layout.addLayout(quick_actions)
        
        # Output section (flexible height)
        self.output_section = OutputSection()
        layout.addWidget(self.output_section, 3)  # Takes 3/10 of space
        
        # Set initial mode
        self._set_mode("encrypt")
    
    def _set_mode(self, mode):
        """Set the operation mode."""
        self.current_mode = mode
        
        if mode == "encrypt":
            # Update button states - selected button should be highlighted
            self.encrypt_mode_btn.setChecked(True)
            self.decrypt_mode_btn.setChecked(False)
            
            # Style the SELECTED button with bright green
            self.encrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3fb950;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 600;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: #56d364;
                }
            """)
            
            # Style the UNSELECTED button as subtle chip
            self.decrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #7d8590;
                    border: 1px solid rgba(48, 54, 61, 0.5);
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 500;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: rgba(240, 136, 62, 0.12);
                    color: #f0883e;
                    border-color: #f0883e;
                }
            """)
            
            self.input_section.set_label("Text to Encrypt")
            self.output_section.set_label("Encrypted Result")
            self.action_btn.setText("Encrypt Now")
            self.action_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3fb950;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 0px 20px;
                    font-size: 12px;
                    font-weight: 600;
                    min-height: 32px;
                    max-height: 32px;
                }
                QPushButton:hover {
                    background-color: #56d364;
                }
                QPushButton:pressed {
                    background-color: #2ea043;
                }
            """)
        else:
            # Update button states
            self.encrypt_mode_btn.setChecked(False)
            self.decrypt_mode_btn.setChecked(True)
            
            # Style the UNSELECTED button as subtle chip
            self.encrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #7d8590;
                    border: 1px solid rgba(48, 54, 61, 0.5);
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 500;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: rgba(63, 185, 80, 0.12);
                    color: #3fb950;
                    border-color: #3fb950;
                }
            """)
            
            # Style the SELECTED button with bright orange
            self.decrypt_mode_btn.setStyleSheet("""
                QPushButton {
                    background-color: #f0883e;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 5px 14px;
                    font-size: 11px;
                    font-weight: 600;
                    min-height: 26px;
                    max-height: 26px;
                }
                QPushButton:hover {
                    background-color: #ff9f66;
                }
            """)
            
            self.input_section.set_label("Text to Decrypt")
            self.output_section.set_label("Decrypted Result")
            self.action_btn.setText("Decrypt Now")
            self.action_btn.setStyleSheet("""
                QPushButton {
                    background-color: #f0883e;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 0px 20px;
                    font-size: 12px;
                    font-weight: 600;
                    min-height: 32px;
                    max-height: 32px;
                }
                QPushButton:hover {
                    background-color: #ff9f66;
                }
                QPushButton:pressed {
                    background-color: #d77735;
                }
            """)
        
        self.mode_changed.emit(mode)
    
    def get_mode(self):
        """Get current mode."""
        return self.current_mode
