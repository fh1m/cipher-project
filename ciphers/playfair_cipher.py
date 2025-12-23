class PlayfairCipher:
    """Playfair Cipher implementation using 5x5 key matrix"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J is omitted, I/J treated as same
    
    def _create_matrix(self, key):
        """Create 5x5 Playfair matrix from key"""
        key = key.upper().replace('J', 'I')
        key_string = ''
        
        # Remove duplicates from key
        for char in key:
            if char in self.alphabet and char not in key_string:
                key_string += char
        
        # Add remaining letters
        for char in self.alphabet:
            if char not in key_string:
                key_string += char
        
        # Create 5x5 matrix
        matrix = []
        for i in range(5):
            matrix.append(list(key_string[i*5:(i+1)*5]))
        
        return matrix
    
    def _find_position(self, matrix, char):
        """Find position of character in matrix"""
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None, None
    
    def _prepare_text(self, text):
        """Prepare text for Playfair cipher (create digraphs), preserving case and space info"""
        # Store original case information and space positions
        case_map = []
        text_clean = ''
        space_positions = []
        current_pos = 0
        original_length = 0
        
        for char in text:
            if char == ' ':
                space_positions.append(current_pos)
            elif char.isalpha():
                case_map.append(char.isupper())
                text_clean += char.upper().replace('J', 'I')
                current_pos += 1
                original_length += 1
        
        prepared = ''
        i = 0
        padding_added = 0
        
        while i < len(text_clean):
            prepared += text_clean[i]
            
            if i + 1 < len(text_clean):
                if text_clean[i] == text_clean[i + 1]:
                    # Same letter repeated, insert X
                    prepared += 'X'
                    case_map.insert(len(prepared) - 1, False)
                    padding_added += 1
                else:
                    prepared += text_clean[i + 1]
                    i += 1
            else:
                # Odd length, add X at the end
                prepared += 'X'
                case_map.append(False)
                padding_added += 1
            
            i += 1
        
        if len(prepared) % 2 != 0:
            prepared += 'X'
            case_map.append(False)
            padding_added += 1
        
        return prepared, case_map, space_positions, original_length
    
    def _restore_spaces(self, text, space_positions):
        """Restore spaces to their original positions"""
        result = list(text)
        for pos in sorted(space_positions, reverse=True):
            if pos <= len(result):
                result.insert(pos, ' ')
        return ''.join(result)
    
    def encrypt(self, plaintext, key):
        """
        Encrypt plaintext using Playfair cipher
        Args:
            plaintext (str): Text to encrypt
            key (str): Keyword for matrix generation
        Returns:
            str: Encrypted ciphertext
        """
        matrix = self._create_matrix(key)
        prepared_text, case_map, space_positions, original_length = self._prepare_text(plaintext)
        ciphertext = ''
        
        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i + 1]
            row1, col1 = self._find_position(matrix, char1)
            row2, col2 = self._find_position(matrix, char2)
            
            if row1 == row2:  # Same row
                enc1 = matrix[row1][(col1 + 1) % 5]
                enc2 = matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                enc1 = matrix[(row1 + 1) % 5][col1]
                enc2 = matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle
                enc1 = matrix[row1][col2]
                enc2 = matrix[row2][col1]
            
            # Apply case from original text
            if i < len(case_map):
                ciphertext += enc1 if case_map[i] else enc1.lower()
            else:
                ciphertext += enc1
            
            if i + 1 < len(case_map):
                ciphertext += enc2 if case_map[i + 1] else enc2.lower()
            else:
                ciphertext += enc2
        
        # Restore spaces
        ciphertext = self._restore_spaces(ciphertext, space_positions)
        
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        """
        Decrypt ciphertext using Playfair cipher
        Args:
            ciphertext (str): Text to decrypt
            key (str): Keyword for matrix generation
        Returns:
            str: Decrypted plaintext
        """
        matrix = self._create_matrix(key)
        # Get only alphabetic characters and preserve case and spaces
        case_map = []
        cipher_clean = ''
        space_positions = []
        current_pos = 0
        
        for char in ciphertext:
            if char == ' ':
                space_positions.append(current_pos)
            elif char.isalpha():
                case_map.append(char.isupper())
                cipher_clean += char.upper().replace('J', 'I')
                current_pos += 1
        
        plaintext = ''
        
        for i in range(0, len(cipher_clean) - 1, 2):
            char1, char2 = cipher_clean[i], cipher_clean[i + 1]
            row1, col1 = self._find_position(matrix, char1)
            row2, col2 = self._find_position(matrix, char2)
            
            if row1 is None or row2 is None:
                continue
            
            if row1 == row2:  # Same row
                dec1 = matrix[row1][(col1 - 1) % 5]
                dec2 = matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                dec1 = matrix[(row1 - 1) % 5][col1]
                dec2 = matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle
                dec1 = matrix[row1][col2]
                dec2 = matrix[row2][col1]
            
            # Apply original case
            plaintext += dec1 if case_map[i] else dec1.lower()
            if i + 1 < len(case_map):
                plaintext += dec2 if case_map[i + 1] else dec2.lower()
        
        # Remove trailing padding X (but only if added as padding, not part of original text)
        # Check the expected length vs actual
        expected_length = len([c for c in ciphertext if c.isalpha()])
        if len(plaintext) > 0 and plaintext[-1].upper() == 'X' and len(plaintext) == expected_length:
            plaintext = plaintext[:-1]
        
        # Restore spaces
        plaintext = self._restore_spaces(plaintext, space_positions)
        
        return plaintext
