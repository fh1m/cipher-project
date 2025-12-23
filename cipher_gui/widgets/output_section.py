"""Output section widget."""

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, 
                              QLabel, QTextEdit, QPushButton)
from PyQt6.QtCore import pyqtSignal, QTimer


class OutputSection(QFrame):
    """Output section with copy and export buttons."""
    
    copy_requested = pyqtSignal()
    export_requested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("section")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        
        # Header
        header = QHBoxLayout()
        icon = QLabel("📤")
        icon.setStyleSheet("font-size: 16px;")
        header.addWidget(icon)
        
        self.label = QLabel("Result")
        self.label.setStyleSheet("font-size: 13px; font-weight: 600; color: #e6edf3;")
        header.addWidget(self.label)
        
        header.addStretch()
        
        copy_btn = QPushButton("📋 Copy")
        copy_btn.setMaximumHeight(28)
        copy_btn.clicked.connect(self.copy_requested.emit)
        copy_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #58a6ff;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 4px 10px;
                font-size: 11px;
                font-weight: 500;
                max-height: 28px;
            }
            QPushButton:hover {
                background-color: #21262d;
                border-color: #58a6ff;
            }
        """)
        header.addWidget(copy_btn)
        
        export_btn = QPushButton("💾")
        export_btn.setToolTip("Export to file")
        export_btn.setFixedSize(28, 28)
        export_btn.clicked.connect(self.export_requested.emit)
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #3fb950;
                border: 1px solid #30363d;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #21262d;
                border-color: #3fb950;
            }
        """)
        header.addWidget(export_btn)
        
        layout.addLayout(header)
        
        # Text edit
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("Results will appear here...")
        self.text_edit.setMinimumHeight(120)
        layout.addWidget(self.text_edit)
    
    def set_label(self, text):
        """Set the section label."""
        self.label.setText(text)
    
    def get_text(self):
        """Get the output text."""
        return self.text_edit.toPlainText()
    
    def set_text(self, text):
        """Set the output text."""
        self.text_edit.setPlainText(text)
    
    def clear(self):
        """Clear the output text."""
        self.text_edit.clear()
    
    def flash_success(self):
        """Flash success indicator."""
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
        """)
        
        QTimer.singleShot(500, lambda: self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 2px solid #3a3a3a;
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
        """))
