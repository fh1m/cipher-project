"""Combined tips and shortcuts card - READABLE VERSION."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt


class TipsShortcutsCard(QFrame):
    """Combined tips and shortcuts card - clear and readable."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tipsCard")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)
        
        # Header - BRIGHT
        header = QLabel("💡 Quick Tips & Shortcuts")
        header.setStyleSheet("""
            font-size: 13px;
            font-weight: 600;
            color: #e6edf3;
            margin-bottom: 6px;
        """)
        layout.addWidget(header)
        
        # Tips section - READABLE
        tips = [
            "✓ Case and spaces are preserved",
            "✓ Validate keys before encrypting",
            "✓ History tracks all operations"
        ]
        
        for tip in tips:
            tip_label = QLabel(tip)
            tip_label.setStyleSheet("""
                color: #c9d1d9;
                font-size: 12px;
                padding: 3px 0px;
                line-height: 1.5;
            """)
            tip_label.setWordWrap(True)
            layout.addWidget(tip_label)
        
        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("background-color: #30363d; max-height: 1px; margin: 10px 0px;")
        layout.addWidget(divider)
        
        # Shortcuts section - BRIGHT & ORGANIZED
        shortcuts = [
            ("Ctrl+O", "Import file"),
            ("Ctrl+S", "Export result"),
            ("Ctrl+L", "Clear all"),
            ("Ctrl+W", "Swap texts"),
            ("Ctrl+H", "View history"),
            ("F1", "Quick guide")
        ]
        
        for key, action in shortcuts:
            shortcut_row = QHBoxLayout()
            shortcut_row.setSpacing(8)
            
            key_label = QLabel(key)
            key_label.setStyleSheet("""
                font-size: 11px;
                color: #58a6ff;
                font-weight: 700;
                background-color: rgba(88, 166, 255, 0.15);
                padding: 3px 8px;
                border-radius: 4px;
                min-width: 60px;
            """)
            key_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            shortcut_row.addWidget(key_label)
            
            action_label = QLabel(action)
            action_label.setStyleSheet("font-size: 12px; color: #c9d1d9;")
            shortcut_row.addWidget(action_label, 1)
            
            layout.addLayout(shortcut_row)
        
        layout.addStretch()
