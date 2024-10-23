class EncDec:
    def __init__(self):
        # Dict to map letters with numbers
        self.lowercase_dict = {chr(i): i - 97 for i in range(97, 123)}
        self.uppercase_dict = {chr(i): i - 65 for i in range(65, 91)}

        # Dicts to map numbers to letters again
        self.reverse_lowercase_dict = {v: k for k, v in self.lowercase_dict.items()}
        self.reverse_uppercase_dict = {v: k for k, v in self.uppercase_dict.items()}

    def cesar_encrypt(self, text, num):
        coded_string = ''
        for c in text:
            if c.isupper():
                # Mapping shifted value back to letter and adding it to a new string
                shifted_value = (self.uppercase_dict[c] + num) % 26
                coded_string += self.reverse_uppercase_dict[shifted_value]
            elif c.islower():
                # Mapping shifted value back to letter and adding it to a new string
                shifted_value = (self.lowercase_dict[c] + num) % 26
                coded_string += self.reverse_lowercase_dict[shifted_value]
            else:
                # Keep non-alphabetic characters unchanged
                coded_string += c

        return coded_string

    ## DECRYPTING SECTION ( TO DO )
    def cesar_decrypt(self, text, num):
        coded_string = ''
        for c in text:
            if c.isupper():
                # Mapping shifted value back to letter and adding it to a new string
                shifted_value = (self.uppercase_dict[c] - num) % 26
                coded_string += self.reverse_uppercase_dict[shifted_value]
            elif c.islower():
                # Mapping shifted value back to letter and adding it to a new string
                shifted_value = (self.lowercase_dict[c] - num) % 26
                coded_string += self.reverse_lowercase_dict[shifted_value]
            else:
                # Keep non-alphabetic characters unchanged
                coded_string += c

        return coded_string