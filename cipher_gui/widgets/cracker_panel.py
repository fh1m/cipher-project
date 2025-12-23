"""Cracker panel for Hill Cipher Known Plaintext Attack."""

from PyQt6.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QTextEdit, QLineEdit, QGroupBox,
                              QScrollArea, QWidget, QSplitter)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cracker import HillCipherCracker


class CrackerPanel(QFrame):
    """Panel for cracking Hill Cipher using known plaintext attack."""
    
    status_message = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("crackerPanel")
        self.cracker = HillCipherCracker()
        self.cracked_key = None
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 16, 20, 16)
        
        # Title
        title = QLabel("Hill Cipher Cracker")
        title.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #f85149;
            padding: 4px 0;
        """)
        layout.addWidget(title)
        
        # Description
        desc = QLabel("Crack 2×2 Hill Cipher keys using Known Plaintext Attack")
        desc.setStyleSheet("color: #8b949e; font-size: 11px; margin-bottom: 4px;")
        layout.addWidget(desc)
        
        # Input section
        input_group = QGroupBox("Known Plaintext-Ciphertext Pair")
        input_group.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        input_layout = QVBoxLayout(input_group)
        input_layout.setSpacing(8)
        input_layout.setContentsMargins(12, 16, 12, 12)
        
        # Plaintext input
        pt_layout = QHBoxLayout()
        pt_label = QLabel("Plaintext:")
        pt_label.setFixedWidth(70)
        pt_label.setStyleSheet("color: #8b949e; font-weight: 500; font-size: 11px;")
        self.plaintext_input = QLineEdit()
        self.plaintext_input.setPlaceholderText("Known plaintext (e.g., hello, attack, secret)")
        self.plaintext_input.setStyleSheet("""
            QLineEdit {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 6px 10px;
                color: #c9d1d9;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #f85149;
            }
        """)
        pt_layout.addWidget(pt_label)
        pt_layout.addWidget(self.plaintext_input)
        input_layout.addLayout(pt_layout)
        
        # Ciphertext input
        ct_layout = QHBoxLayout()
        ct_label = QLabel("Ciphertext:")
        ct_label.setFixedWidth(70)
        ct_label.setStyleSheet("color: #8b949e; font-weight: 500; font-size: 11px;")
        self.ciphertext_input = QLineEdit()
        self.ciphertext_input.setPlaceholderText("Corresponding ciphertext")
        self.ciphertext_input.setStyleSheet("""
            QLineEdit {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 6px 10px;
                color: #c9d1d9;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #f85149;
            }
        """)
        ct_layout.addWidget(ct_label)
        ct_layout.addWidget(self.ciphertext_input)
        input_layout.addLayout(ct_layout)
        
        layout.addWidget(input_group)
        
        # Action buttons - slimmer
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        
        self.crack_btn = QPushButton("Crack Key")
        self.crack_btn.setStyleSheet("""
            QPushButton {
                background-color: #f85149;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #ff6b6b;
            }
            QPushButton:pressed {
                background-color: #da3633;
            }
        """)
        self.crack_btn.clicked.connect(self.crack_key)
        btn_layout.addWidget(self.crack_btn)
        
        self.analyze_btn = QPushButton("Analyze")
        self.analyze_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #58a6ff;
                border: 1px solid #58a6ff;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(88, 166, 255, 0.1);
            }
        """)
        self.analyze_btn.clicked.connect(self.analyze_plaintext)
        btn_layout.addWidget(self.analyze_btn)
        
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7d8590;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(125, 133, 144, 0.1);
                border-color: #7d8590;
            }
        """)
        self.clear_btn.clicked.connect(self.clear_all)
        btn_layout.addWidget(self.clear_btn)
        
        layout.addLayout(btn_layout)
        
        # Results section - takes more space
        result_group = QGroupBox("Results")
        result_group.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        result_layout = QVBoxLayout(result_group)
        result_layout.setContentsMargins(12, 16, 12, 12)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(200)
        self.result_text.setStyleSheet("""
            QTextEdit {
                background-color: #0d1117;
                border: 1px solid #21262d;
                border-radius: 4px;
                padding: 10px;
                color: #c9d1d9;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 12px;
                line-height: 1.4;
            }
        """)
        result_layout.addWidget(self.result_text)
        
        layout.addWidget(result_group, 1)  # Stretch factor
        
        # Decrypt with cracked key section
        decrypt_group = QGroupBox("Decrypt with Cracked Key")
        decrypt_group.setStyleSheet("""
            QGroupBox {
                font-weight: 600;
                font-size: 12px;
                color: #c9d1d9;
                border: 1px solid #30363d;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 6px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
            }
        """)
        decrypt_layout = QVBoxLayout(decrypt_group)
        decrypt_layout.setSpacing(8)
        decrypt_layout.setContentsMargins(12, 16, 12, 12)
        
        # Ciphertext to decrypt
        dec_ct_layout = QHBoxLayout()
        dec_ct_label = QLabel("Ciphertext:")
        dec_ct_label.setFixedWidth(70)
        dec_ct_label.setStyleSheet("color: #8b949e; font-weight: 500; font-size: 11px;")
        self.decrypt_input = QLineEdit()
        self.decrypt_input.setPlaceholderText("Enter any ciphertext to decrypt")
        self.decrypt_input.setStyleSheet("""
            QLineEdit {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 4px;
                padding: 6px 10px;
                color: #c9d1d9;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #3fb950;
            }
        """)
        dec_ct_layout.addWidget(dec_ct_label)
        dec_ct_layout.addWidget(self.decrypt_input)
        decrypt_layout.addLayout(dec_ct_layout)
        
        # Decrypt button and result
        dec_btn_layout = QHBoxLayout()
        dec_btn_layout.setSpacing(8)
        
        self.decrypt_btn = QPushButton("Decrypt")
        self.decrypt_btn.setEnabled(False)
        self.decrypt_btn.setFixedWidth(80)
        self.decrypt_btn.setStyleSheet("""
            QPushButton {
                background-color: #3fb950;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 11px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #56d364;
            }
            QPushButton:disabled {
                background-color: #21262d;
                color: #484f58;
            }
        """)
        self.decrypt_btn.clicked.connect(self.decrypt_with_key)
        dec_btn_layout.addWidget(self.decrypt_btn)
        
        self.decrypt_result = QLineEdit()
        self.decrypt_result.setReadOnly(True)
        self.decrypt_result.setPlaceholderText("Decrypted result")
        self.decrypt_result.setStyleSheet("""
            QLineEdit {
                background-color: #0d1117;
                border: 1px solid #21262d;
                border-radius: 4px;
                padding: 6px 10px;
                color: #3fb950;
                font-size: 12px;
                font-weight: 500;
            }
        """)
        dec_btn_layout.addWidget(self.decrypt_result, 1)
        decrypt_layout.addLayout(dec_btn_layout)
        
        layout.addWidget(decrypt_group)
    
    def crack_key(self):
        """Attempt to crack the Hill cipher key."""
        plaintext = self.plaintext_input.text().strip()
        ciphertext = self.ciphertext_input.text().strip()
        
        if not plaintext or not ciphertext:
            self.result_text.setHtml(
                '<span style="color: #f85149;">Error: Both plaintext and ciphertext are required</span>'
            )
            self.status_message.emit("Error: Missing input")
            return
        
        # Capture output
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = captured = io.StringIO()
        
        try:
            self.cracked_key = self.cracker.crack_key(plaintext, ciphertext)
        finally:
            sys.stdout = old_stdout
        
        output = captured.getvalue()
        
        if self.cracked_key is not None:
            # Format result
            key_flat = ','.join(str(int(x)) for x in self.cracked_key.flatten())
            det = self.cracker._det_2x2(
                self.cracked_key[0,0], self.cracked_key[0,1],
                self.cracked_key[1,0], self.cracked_key[1,1]
            )
            
            # Verify by decrypting
            decrypted = self.cracker.decrypt(ciphertext, self.cracked_key)
            
            # Method used
            method = "Brute Force" if "brute force" in output.lower() else "Algebraic"
            
            result_html = f'''
<div style="font-family: Consolas, Monaco, monospace; line-height: 1.6;">
<span style="color: #3fb950; font-weight: bold; font-size: 13px;">KEY CRACKED SUCCESSFULLY</span><br><br>
<table style="border-collapse: collapse;">
<tr><td style="color: #8b949e; padding-right: 12px;">Key Matrix:</td>
<td style="color: #f0883e; font-weight: 500;">[ {int(self.cracked_key[0,0]):2d}  {int(self.cracked_key[0,1]):2d} ]<br>[ {int(self.cracked_key[1,0]):2d}  {int(self.cracked_key[1,1]):2d} ]</td></tr>
<tr><td style="color: #8b949e; padding-right: 12px;">Flat Array:</td>
<td style="color: #58a6ff;">[{key_flat}]</td></tr>
<tr><td style="color: #8b949e; padding-right: 12px;">Determinant:</td>
<td style="color: #bc8cff;">{det} (mod 26)</td></tr>
<tr><td style="color: #8b949e; padding-right: 12px;">Method:</td>
<td style="color: #7d8590;">{method}</td></tr>
</table>
<br>
<span style="color: #8b949e;">Verification:</span> <span style="color: #c9d1d9;">{ciphertext.upper()}</span> → <span style="color: #3fb950; font-weight: bold;">{decrypted}</span>
</div>
'''
            self.result_text.setHtml(result_html)
            self.decrypt_btn.setEnabled(True)
            self.status_message.emit(f"Key cracked: [{key_flat}]")
        else:
            self.result_text.setHtml(
                '<span style="color: #f85149;">Failed to crack key</span><br><br>'
                '<span style="color: #8b949e;">Possible issues:</span><br>'
                '<span style="color: #7d8590;">• Incorrect plaintext-ciphertext pair<br>'
                '• Texts don\'t correspond to the same encryption<br>'
                '• Use Analyze to check plaintext invertibility</span>'
            )
            self.decrypt_btn.setEnabled(False)
            self.cracked_key = None
            self.status_message.emit("Failed to crack key")
    
    def analyze_plaintext(self):
        """Analyze plaintext for invertibility."""
        plaintext = self.plaintext_input.text().strip()
        
        if not plaintext:
            self.result_text.setHtml(
                '<span style="color: #f85149;">Enter plaintext to analyze</span>'
            )
            return
        
        # Get digraphs and analyze
        digraphs = self.cracker._text_to_digraphs(plaintext)
        n = len(digraphs)
        
        cleaned = self.cracker._pad_text(self.cracker._clean_text(plaintext))
        
        result_html = f'''
<div style="font-family: Consolas, Monaco, monospace; line-height: 1.5;">
<span style="color: #58a6ff; font-weight: bold;">PLAINTEXT ANALYSIS</span><br><br>
<span style="color: #8b949e;">Input:</span> <span style="color: #c9d1d9;">{plaintext}</span><br>
<span style="color: #8b949e;">Processed:</span> <span style="color: #c9d1d9;">{cleaned}</span><br>
<span style="color: #8b949e;">Digraphs:</span> <span style="color: #bc8cff;">{len(digraphs)}</span><br><br>
<span style="color: #8b949e;">Matrix Pairs:</span><br>
'''
        
        from itertools import combinations
        invertible_count = 0
        
        if n < 2:
            result_html += '<span style="color: #f0883e;">Need at least 4 characters (2 digraphs)</span>'
        else:
            for i, j in combinations(range(n), 2):
                p1, p2 = digraphs[i]
                p3, p4 = digraphs[j]
                det = self.cracker._det_2x2(p1, p3, p2, p4)
                invertible = det in self.cracker.VALID_DETS
                if invertible:
                    invertible_count += 1
                    status = '<span style="color: #3fb950;">✓</span>'
                else:
                    status = '<span style="color: #f85149;">✗</span>'
                result_html += f'<span style="color: #7d8590;">  ({i},{j}) det={det:2d} {status}</span><br>'
        
            result_html += f'''<br>
<span style="color: #8b949e;">Invertible Pairs:</span> <span style="color: #f0883e;">{invertible_count}</span><br>
'''
            if invertible_count > 0:
                result_html += '<span style="color: #3fb950;">Algebraic attack possible</span>'
            else:
                result_html += '<span style="color: #f0883e;">Brute force required</span>'
        
        result_html += '</div>'
        self.result_text.setHtml(result_html)
        self.status_message.emit(f"Analysis: {invertible_count} invertible pairs")
    
    def decrypt_with_key(self):
        """Decrypt additional ciphertext with cracked key."""
        if self.cracked_key is None:
            return
        
        ciphertext = self.decrypt_input.text().strip()
        if not ciphertext:
            self.decrypt_result.setText("")
            return
        
        decrypted = self.cracker.decrypt(ciphertext, self.cracked_key)
        if decrypted:
            self.decrypt_result.setText(decrypted)
            self.status_message.emit(f"Decrypted: {decrypted}")
        else:
            self.decrypt_result.setText("Error")
    
    def clear_all(self):
        """Clear all fields."""
        self.plaintext_input.clear()
        self.ciphertext_input.clear()
        self.result_text.clear()
        self.decrypt_input.clear()
        self.decrypt_result.clear()
        self.cracked_key = None
        self.decrypt_btn.setEnabled(False)
        self.status_message.emit("Cleared")
