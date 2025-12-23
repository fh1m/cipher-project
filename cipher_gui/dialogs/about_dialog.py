"""About dialog."""

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PyQt6.QtCore import Qt


class AboutDialog(QDialog):
    """About dialog with app information."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Classical Cipher Tool")
        self.setFixedSize(500, 400)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Logo
        logo = QLabel("🔐")
        logo.setStyleSheet("font-size: 64px;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        # Title
        title = QLabel("Classical Cipher Tool")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Version
        version = QLabel("Version 1.0")
        version.setStyleSheet("font-size: 14px; color: #888; margin-bottom: 20px;")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version)
        
        # Description
        desc = QLabel(
            "A modern, user-friendly application for classical cryptography.\n\n"
            "Features:\n"
            "• Caesar, Affine, Playfair, and Hill ciphers\n"
            "• Hill Cipher Known Plaintext Attack cracker\n"
            "• Beautiful dark-themed interface\n"
            "• History tracking\n"
            "• Import/Export functionality\n"
            "• Real-time validation\n"
            "• Keyboard shortcuts"
        )
        desc.setStyleSheet("color: #ccc; font-size: 13px; line-height: 1.5;")
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        layout.addStretch()
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        
        self.setStyleSheet("""
            QDialog {
                background-color: #161b22;
            }
            QDialogButtonBox QPushButton {
                background-color: #21262d;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 6px;
                padding: 8px 20px;
                min-width: 80px;
                min-height: 32px;
                max-height: 36px;
                font-weight: 500;
                font-size: 13px;
            }
            QDialogButtonBox QPushButton:hover {
                background-color: #58a6ff;
                border-color: #58a6ff;
                color: #ffffff;
            }
        """)
