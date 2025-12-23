"""Perfect, professional dark theme - Figma quality."""

from PyQt6.QtGui import QColor


class Theme:
    """Figma-quality dark theme with perfect spacing and aesthetics."""
    
    # Colors - Professional palette
    BG_DARK = "#0d1117"
    BG_MEDIUM = "#161b22"
    BG_ELEVATED = "#21262d"
    
    BORDER = "#30363d"
    
    TEXT_PRIMARY = "#e6edf3"
    TEXT_SECONDARY = "#7d8590"
    TEXT_DISABLED = "#484f58"
    
    ACCENT_BLUE = "#58a6ff"
    SUCCESS = "#3fb950"
    WARNING = "#f0883e"
    ERROR = "#f85149"
    
    @staticmethod
    def get_stylesheet():
        """Perfect stylesheet with no cut-offs and great spacing."""
        return """
            /* ==================== GLOBAL ==================== */
            * {
                font-family: -apple-system, 'Segoe UI', 'SF Pro Display', 'Roboto', 'Ubuntu', 'Arial', sans-serif;
                outline: none;
            }
            
            QMainWindow {
                background-color: #0d1117;
            }
            
            /* ==================== MENU & TOOLBAR ==================== */
            QMenuBar {
                background-color: #161b22;
                color: #e6edf3;
                border: none;
                padding: 6px 10px;
            }
            
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 14px;
                border-radius: 6px;
                margin: 0px 2px;
            }
            
            QMenuBar::item:selected {
                background-color: rgba(88, 166, 255, 0.15);
                color: #58a6ff;
            }
            
            QMenu {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 10px;
                padding: 6px;
            }
            
            QMenu::item {
                padding: 10px 28px 10px 14px;
                border-radius: 6px;
                margin: 2px 4px;
            }
            
            QMenu::item:selected {
                background-color: rgba(88, 166, 255, 0.15);
                color: #58a6ff;
            }
            
            QToolBar {
                background-color: #161b22;
                border: none;
                spacing: 8px;
                padding: 8px;
            }
            
            QToolBar QToolButton {
                background-color: transparent;
                color: #7d8590;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: 500;
            }
            
            QToolBar QToolButton:hover {
                background-color: rgba(88, 166, 255, 0.15);
                color: #58a6ff;
                border-color: #58a6ff;
            }
            
            /* ==================== FRAMES - Perfect Cards ==================== */
            QFrame#header {
                background-color: #161b22;
                border-bottom: 1px solid #30363d;
            }
            
            QFrame#panel {
                background-color: transparent;
                border: none;
            }
            
            QFrame#section {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
            
            QFrame#modeContainer {
                background-color: transparent;
                border: none;
            }
            
            QFrame#infoCard, QFrame#tipsCard, QFrame#shortcutsCard {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
            
            /* ==================== LABELS ==================== */
            QLabel {
                color: #e6edf3;
                background-color: transparent;
            }
            
            /* ==================== TEXT INPUTS - PERFECT ROUNDED ==================== */
            QTextEdit {
                background-color: #0d1117;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 12px;
                padding: 16px;
                font-size: 14px;
                font-family: 'SF Mono', 'Monaco', 'Consolas', 'Courier New', monospace;
                selection-background-color: rgba(88, 166, 255, 0.3);
                line-height: 1.6;
                min-height: 120px;
            }
            
            QTextEdit:hover {
                border-color: #58a6ff;
            }
            
            QTextEdit:focus {
                border-color: #58a6ff;
                border-width: 2px;
                padding: 15px;
            }
            
            QTextEdit:read-only {
                background-color: #0d1117;
                color: #7d8590;
            }
            
            QLineEdit {
                background-color: #161b22;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 14px;
                font-family: -apple-system, 'Segoe UI', 'SF Pro Display', 'Roboto', 'Ubuntu', sans-serif;
                selection-background-color: rgba(88, 166, 255, 0.3);
                min-height: 38px;
                max-height: 38px;
            }
            
            QLineEdit:hover {
                border-color: #58a6ff;
            }
            
            QLineEdit:focus {
                border-color: #58a6ff;
                border-width: 2px;
                padding: 9px 13px;
            }
            
            /* ==================== CHECKBOXES ==================== */
            QCheckBox {
                color: #e6edf3;
                spacing: 10px;
                padding: 4px;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #30363d;
                border-radius: 6px;
                background-color: transparent;
            }
            
            QCheckBox::indicator:hover {
                border-color: #58a6ff;
                background-color: rgba(88, 166, 255, 0.1);
            }
            
            QCheckBox::indicator:checked {
                background-color: #58a6ff;
                border-color: #58a6ff;
            }
            
            /* ==================== SCROLLBARS - Minimal ==================== */
            QScrollBar:vertical {
                background-color: transparent;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #30363d;
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #484f58;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                height: 0px;
                background: none;
            }
            
            QScrollBar:horizontal {
                background-color: transparent;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background-color: #30363d;
                border-radius: 6px;
                min-width: 30px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background-color: #484f58;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                width: 0px;
                background: none;
            }
            
            /* ==================== STATUS BAR ==================== */
            QStatusBar {
                background-color: #161b22;
                color: #7d8590;
                border-top: 1px solid #30363d;
                font-size: 12px;
                padding: 6px 12px;
            }
            
            /* ==================== DIALOGS ==================== */
            QDialog {
                background-color: #161b22;
            }
            
            QMessageBox {
                background-color: #161b22;
            }
            
            QMessageBox QLabel {
                color: #e6edf3;
                min-width: 350px;
                padding: 10px;
            }
            
            /* ==================== TOOLTIPS ==================== */
            QToolTip {
                background-color: #21262d;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 12px;
            }
        """
    
    @staticmethod
    def adjust_brightness(hex_color, factor):
        """Adjust color brightness."""
        color = QColor(hex_color)
        h, s, l, a = color.getHslF()
        l = min(1.0, max(0.0, l * factor))
        color.setHslF(h, s, l, a)
        return color.name()
