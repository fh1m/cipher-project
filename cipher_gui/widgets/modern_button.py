"""Modern button widget with smooth animations and hover effects."""

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QSize


class ModernButton(QPushButton):
    """Modern flat button with smooth hover effects and animations."""
    
    def __init__(self, text, color="#58a6ff", icon_text=""):
        super().__init__(text)
        self.base_color = color
        self.hover_color = self.adjust_brightness(color, 1.15)
        self.pressed_color = self.adjust_brightness(color, 0.85)
        self.icon_text = icon_text
        self.setup_style()
    
    def setup_style(self):
        """Setup modern button styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.base_color};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
                min-height: 32px;
                max-height: 36px;
            }}
            QPushButton:hover {{
                background-color: {self.hover_color};
            }}
            QPushButton:pressed {{
                background-color: {self.pressed_color};
            }}
            QPushButton:disabled {{
                background-color: #30363d;
                color: #6e7681;
            }}
        """)
        
        # Set consistent size
        self.setMinimumHeight(32)
        self.setMaximumHeight(36)
    
    @staticmethod
    def adjust_brightness(hex_color, factor):
        """Adjust color brightness for hover/pressed states."""
        color = QColor(hex_color)
        h, s, l, a = color.getHslF()
        l = min(1.0, max(0.0, l * factor))
        color.setHslF(h, s, l, a)
        return color.name()
