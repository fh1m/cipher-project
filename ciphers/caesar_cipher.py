class CaesarCipher:
    """Caesar Cipher implementation with shift-based encryption/decryption"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Caesar cipher
        Args:
            plaintext (str): Text to encrypt
            key (int): Shift value (0-25)
        Returns:
            str: Encrypted ciphertext
        """
        key = int(key) % 26
        ciphertext = ''
        
        for char in plaintext:
            if char.upper() in self.alphabet:
                old_index = self.alphabet.index(char.upper())
                new_index = (old_index + key) % 26
                new_char = self.alphabet[new_index]
                ciphertext += new_char if char.isupper() else new_char.lower()
            else:
                ciphertext += char
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Caesar cipher
        Args:
            ciphertext (str): Text to decrypt
            key (int): Shift value (0-25)
        Returns:
            str: Decrypted plaintext
        """
        key = int(key) % 26
        plaintext = ''
        
        for char in ciphertext:
            if char.upper() in self.alphabet:
                old_index = self.alphabet.index(char.upper())
                new_index = (old_index - key) % 26
                new_char = self.alphabet[new_index]
                plaintext += new_char if char.isupper() else new_char.lower()
            else:
                plaintext += char
        
        return plaintext
