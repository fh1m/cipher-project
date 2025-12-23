"""Input text section widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal


class InputSection(QFrame):
    """Input text section with character counter and import button."""
    
    import_requested = pyqtSignal()
    text_changed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("📝")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        self.label = QLabel("Text to Encrypt")
        self.label.setStyleSheet("font-size: 13px; font-weight: 600; color: #e6edf3;")
        header.addWidget(self.label)
        
        header.addStretch()
        
        self.char_count_label = QLabel("0 chars")
        self.char_count_label.setStyleSheet("font-size: 11px; color: #6e7681;")
        header.addWidget(self.char_count_label)
        
        import_btn = QPushButton("📂")
        import_btn.setToolTip("Import from file")
        import_btn.setFixedSize(28, 28)
        import_btn.clicked.connect(self.import_requested.emit)
        import_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #58a6ff;
                border: 1px solid #30363d;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #21262d;
                border-color: #58a6ff;
            }
        """)
        header.addWidget(import_btn)
        
        layout.addLayout(header)
        
        # Text edit
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter your message here...")
        self.text_edit.textChanged.connect(self._on_text_changed)
        self.text_edit.setMinimumHeight(120)
        layout.addWidget(self.text_edit)
    
    def _on_text_changed(self):
        count = len(self.text_edit.toPlainText())
        self.char_count_label.setText(f"{count} chars")
        self.text_changed.emit()
    
    def set_label(self, text):
        """Set the section label."""
        self.label.setText(text)
    
    def get_text(self):
        """Get the input text."""
        return self.text_edit.toPlainText().strip()
    
    def set_text(self, text):
        """Set the input text."""
        self.text_edit.setPlainText(text)
    
    def clear(self):
        """Clear the input text."""
        self.text_edit.clear()
