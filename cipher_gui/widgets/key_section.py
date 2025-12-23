"""Key input section widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import pyqtSignal


class KeySection(QFrame):
    """Key input section with validation indicator."""
    
    key_changed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("🔑")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        title = QLabel("Encryption Key")
        title.setStyleSheet("font-size: 13px; font-weight: 600; color: #e6edf3; margin-left: 6px;")
        header.addWidget(title)
        header.addStretch()
        
        layout.addLayout(header)
        
        # Key input
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter key...")
        self.key_input.textChanged.connect(self.key_changed.emit)
        layout.addWidget(self.key_input)
        
        # Key help - RIGHT BELOW input, readable
        self.key_help_text = QLabel()
        self.key_help_text.setWordWrap(True)
        self.key_help_text.setStyleSheet("""
            color: #7d8590;
            font-size: 11px;
            background-color: rgba(88, 166, 255, 0.06);
            padding: 8px 10px;
            border-radius: 6px;
            border-left: 2px solid #58a6ff;
            margin-top: 6px;
        """)
        layout.addWidget(self.key_help_text)
        
        # Key validation indicator - compact
        self.key_validation = QLabel()
        self.key_validation.setStyleSheet("font-size: 11px; color: #7d8590; margin-top: 4px;")
        layout.addWidget(self.key_validation)
    
    def set_key_help(self, help_data):
        """Set key help information."""
        if isinstance(help_data, dict):
            format_text = help_data.get('format', '')
            example_text = help_data.get('example', '')
            tip_text = help_data.get('tip', help_data.get('details', ''))
            
            help_text = ""
            if format_text:
                help_text += f"<b>Format:</b> {format_text}<br>"
            if example_text:
                help_text += f"<b>Example:</b> <code style='background-color: #1c2128; padding: 2px 6px; border-radius: 3px;'>{example_text}</code><br>"
            if tip_text:
                help_text += f"<b>Tip:</b> {tip_text}"
            
            self.key_help_text.setText(help_text)
            if example_text:
                self.key_input.setPlaceholderText(f"e.g., {example_text}")
        else:
            self.key_help_text.setText(str(help_data))
            self.key_input.setPlaceholderText("Enter key...")
    
    def get_key(self):
        """Get the key text."""
        return self.key_input.text().strip()
    
    def set_validation(self, is_valid, message=""):
        """Set validation status."""
        if not message:
            self.key_validation.setText("")
        elif is_valid:
            self.key_validation.setText(f"✓ {message}")
            self.key_validation.setStyleSheet("color: #4CAF50; font-size: 11px;")
        else:
            self.key_validation.setText(f"✗ {message}")
            self.key_validation.setStyleSheet("color: #f44336; font-size: 11px;")
    
    def clear(self):
        """Clear the key input."""
        self.key_input.clear()
        self.key_validation.setText("")
