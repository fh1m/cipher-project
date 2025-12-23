"""History dialog."""

from datetime import datetime
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                              QScrollArea, QWidget, QFrame, QMessageBox)
from PyQt6.QtCore import Qt
from cipher_gui.widgets.modern_button import ModernButton


class HistoryDialog(QDialog):
    """Dialog to view operation history."""
    
    def __init__(self, history_manager, parent=None):
        super().__init__(parent)
        self.history_manager = history_manager
        self.setWindowTitle("Operation History")
        self.setMinimumSize(700, 500)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("📜 Recent Operations")
        header.setStyleSheet("font-size: 18px; font-weight: bold; color: #fff; padding: 10px;")
        layout.addWidget(header)
        
        # History list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: 1px solid #444;
                border-radius: 8px;
                background-color: #1e1e1e;
            }
        """)
        
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(10)
        
        history = self.history_manager.get_history()
        if not history:
            no_history = QLabel("No history yet. Start encrypting or decrypting!")
            no_history.setStyleSheet("color: #888; padding: 20px; font-size: 14px;")
            no_history.setAlignment(Qt.AlignmentFlag.AlignCenter)
            content_layout.addWidget(no_history)
        else:
            for entry in history:
                item = self.create_history_item(entry)
                content_layout.addWidget(item)
        
        content_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        clear_btn = ModernButton("🗑️ Clear History", "#f44336")
        clear_btn.clicked.connect(self.clear_history)
        btn_layout.addWidget(clear_btn)
        
        btn_layout.addStretch()
        
        close_btn = ModernButton("Close", "#666")
        close_btn.clicked.connect(self.accept)
        btn_layout.addWidget(close_btn)
        
        layout.addLayout(btn_layout)
        
        self.setStyleSheet("""
            QDialog {
                background-color: #161b22;
            }
        """)
    
    def create_history_item(self, entry):
        """Create a history item widget."""
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #21262d;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 10px;
            }
            QFrame:hover {
                border: 1px solid #58a6ff;
                background-color: #2d333b;
            }
        """)
        
        layout = QVBoxLayout(frame)
        
        # Header
        header_layout = QHBoxLayout()
        
        mode_icon = "🔒" if entry['mode'] == 'encrypt' else "🔓"
        mode_label = QLabel(f"{mode_icon} {entry['mode'].upper()}")
        mode_label.setStyleSheet("font-weight: bold; color: #4CAF50;" if entry['mode'] == 'encrypt' else "font-weight: bold; color: #FF9800;")
        header_layout.addWidget(mode_label)
        
        cipher_label = QLabel(f"• {entry['cipher']}")
        cipher_label.setStyleSheet("color: #2196F3;")
        header_layout.addWidget(cipher_label)
        
        header_layout.addStretch()
        
        time_label = QLabel(datetime.fromisoformat(entry['timestamp']).strftime("%Y-%m-%d %H:%M:%S"))
        time_label.setStyleSheet("color: #888; font-size: 11px;")
        header_layout.addWidget(time_label)
        
        layout.addLayout(header_layout)
        
        # Content
        key_label = QLabel(f"Key: {entry['key']}")
        key_label.setStyleSheet("color: #aaa; font-size: 12px;")
        layout.addWidget(key_label)
        
        input_label = QLabel(f"Input: {entry['input']}")
        input_label.setStyleSheet("color: #ccc; font-size: 12px; font-family: monospace;")
        input_label.setWordWrap(True)
        layout.addWidget(input_label)
        
        output_label = QLabel(f"Output: {entry['output']}")
        output_label.setStyleSheet("color: #ccc; font-size: 12px; font-family: monospace;")
        output_label.setWordWrap(True)
        layout.addWidget(output_label)
        
        return frame
    
    def clear_history(self):
        """Clear all history."""
        reply = QMessageBox.question(
            self, 
            "Clear History", 
            "Are you sure you want to clear all history?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.history_manager.clear_history()
            self.accept()
            QMessageBox.information(self, "Success", "History cleared successfully!")
