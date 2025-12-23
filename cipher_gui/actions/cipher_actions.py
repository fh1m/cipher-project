"""Cipher operations (encrypt/decrypt)."""

from cipher_gui.utils.helpers import show_error


class CipherActions:
    """Handles cipher encryption and decryption operations."""
    
    def __init__(self, parent):
        self.parent = parent
    
    def encrypt(self, cipher, text, key):
        """
        Encrypt text with the given cipher and key.
        
        Args:
            cipher: The cipher instance
            text: Text to encrypt
            key: Encryption key
            
        Returns:
            str: Encrypted text, or None if error
        """
        if not text:
            show_error(self.parent, "Please enter text to encrypt", "Empty Input")
            return None
        
        if not key:
            show_error(self.parent, "Please enter an encryption key", "Missing Key")
            return None
        
        try:
            result = cipher.encrypt(text, key)
            return result
        except ValueError as e:
            show_error(self.parent, str(e), "Encryption Error")
            return None
        except Exception as e:
            show_error(self.parent, f"Unexpected error: {str(e)}", "Error")
            return None
    
    def decrypt(self, cipher, text, key):
        """
        Decrypt text with the given cipher and key.
        
        Args:
            cipher: The cipher instance
            text: Text to decrypt
            key: Decryption key
            
        Returns:
            str: Decrypted text, or None if error
        """
        if not text:
            show_error(self.parent, "Please enter text to decrypt", "Empty Input")
            return None
        
        if not key:
            show_error(self.parent, "Please enter the decryption key", "Missing Key")
            return None
        
        try:
            result = cipher.decrypt(text, key)
            return result
        except ValueError as e:
            show_error(self.parent, str(e), "Decryption Error")
            return None
        except Exception as e:
            show_error(self.parent, f"Unexpected error: {str(e)}", "Error")
            return None
