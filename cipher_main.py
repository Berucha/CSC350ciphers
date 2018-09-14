######################################################################
# Author: Berucha Cintron
# Username: cintronb
#
#
# Purpose: The class imports a file, encrypts the file, and exports the cipher to a new file.
#           Also implementing the decrypt function.
#######################################################################
# Acknowledgements: The original code was created by Dr. Scott Heggen
#                       and modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


class CaesarCipher:
    '''
    A class that encrypts and decrypts messages.
    '''

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # The alphabet, which will be used to do our shifts

    def __init__(self, input_file="message_input.txt", key=0, crypt_type="encrypt"):
        """
        A constructor for the CaesarCipher class

        :param input_file: The file to be encrypted/decrypted
        :param key: The amount each message/cipher needs shifted
        :param crypt_type: Either encrypt or decrypt
        """
        self.input_file = input_file  # The file to be encrypted or decrypted
        self.key = key  # The amount each message/cipher will be shifted
        self.message = ""  # A placeholder for the message
        self.cipher = ""  # A placeholder for the cipher
        self.crypt_type = crypt_type  # Either "encrypt" or "decrypt"
        self.import_file()  # Calls the import_file() method below

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":  # If the file is meant to be encrypted, do the following
            self.message = f.read()  # Set self.message to the file contents
        elif self.crypt_type == "decrypt": # If the file is meant to be decrypted, do the following
            self.cipher = f.read()  # Set self.cipher to the file contents
        f.close()
        if __name__ == "__main__":
            print("File imported: {0}".format(self.input_file))

    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        if __name__ == "__main__":
            print("File exported: {0}".format(filename))

    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key
        :return: a string representing the ciphertext
        """
        output = ""
        for i in self.message:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the beginning of the alphabet)
                output += self.alphabet[(old_letter + self.key) % 26]
            else:
                output += i  # Adds non-alphabet characters directly
        if __name__ == "__main__":
            print("Message Encrypted")
        return output

    def decrypt(self):
        """
        Converts a ciphertext into an original message by shifting each letter to the left by the key

        :return: a string representing the original message
        """
        output = ""
        for i in self.cipher:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                output += self.alphabet[(old_letter - self.key) % 26]
            else:
                output += i  # Adds non-alphabet characters directly
        if __name__ == "__main__":
            print("Message Decrypted")
        return output


def main():
    # A sample encryption
    cipher0 = CaesarCipher("message_input.txt", 2, "encrypt")  # Constructs a new CaesarCipher object called cipher0
    cipher_text0 = cipher0.encrypt()  # Encrypts the file specified in the constructor
    cipher0.export_file(cipher_text0, "cipher_sample.txt")  # Writes the output to a file

    # Caesar has some letters to send and receive.
    # Letter 1 goes to P. Lentulus Spinther, who has agreed with Caesar to use a key of 3
    cipher_Lentulus = CaesarCipher("letter_to_friend_1.txt", 3, "encrypt") # Constructs a new CaesarCipher object called cipher_Lentulus
    Lentulus_text = cipher_Lentulus.encrypt() # Encrypts the file specified in the constructor
    cipher_Lentulus.export_file(Lentulus_text, "cipher_to_friend_1.txt") # Writes the output to a file

    # Letter 2 goes to Marcus Tullius Cicero, who has agreed to use a key of 14
    cipher_marcus = CaesarCipher("letter_to_friend_2.txt", 14, "encrypt")  # Constructs a new CaesarCipher object called cipher_marcus
    marcus_text = cipher_marcus.encrypt() # Encrypts the file specified in the constructor
    cipher_marcus.export_file(marcus_text, "cipher_to_friend_2.txt") # Writes the output to a file

    # Letter 3 is coming from Cicero for Caesar to decrypt. Again, they agreed to use key 14
    cipher3 = CaesarCipher("cipher_from_friend_3.txt", 14, "decrypt")  # constructs a new CaesarCipher object called cipher3
    cipher3_text = cipher3.decrypt() # Decrypts the file specified in the constructor
    cipher3.export_file(cipher3_text, "message_from_friend_3.txt")  # Writes the output to a file


if __name__ == "__main__":
    main()
