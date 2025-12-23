"""Keyboard shortcuts card widget."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel


class ShortcutsCard(QFrame):
    """Displays keyboard shortcuts."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("shortcutsCard")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        
        header = QLabel("⌨️ Shortcuts")
        header.setStyleSheet("font-size: 14px; font-weight: bold; color: #fff;")
        layout.addWidget(header)
        
        shortcuts = [
            ("Ctrl+O", "Import file"),
            ("Ctrl+S", "Export result"),
            ("Ctrl+L", "Clear all"),
            ("Ctrl+W", "Swap texts"),
            ("Ctrl+H", "View history"),
            ("F1", "Quick guide")
        ]
        
        for key, desc in shortcuts:
            row = QHBoxLayout()
            
            key_label = QLabel(key)
            key_label.setStyleSheet("""
                color: #2196F3;
                font-size: 11px;
                font-weight: bold;
                background-color: rgba(33, 150, 243, 0.1);
                padding: 3px 8px;
                border-radius: 3px;
                border: 1px solid #2196F3;
            """)
            key_label.setFixedWidth(70)
            row.addWidget(key_label)
            
            desc_label = QLabel(desc)
            desc_label.setStyleSheet("color: #aaa; font-size: 11px;")
            row.addWidget(desc_label, 1)
            
            layout.addLayout(row)
