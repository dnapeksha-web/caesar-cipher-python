import string

class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26
        self.alphabet_lower = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase

    def encrypt(self, text: str) -> str:
        return self._transform(text, self.shift)

    def decrypt(self, text: str) -> str:
        return self._transform(text, -self.shift)

    def _transform(self, text: str, shift: int) -> str:
        result = []

        for char in text:
            if char in self.alphabet_lower:
                index = (self.alphabet_lower.index(char) + shift) % 26
                result.append(self.alphabet_lower[index])

            elif char in self.alphabet_upper:
                index = (self.alphabet_upper.index(char) + shift) % 26
                result.append(self.alphabet_upper[index])

            else:
                # Keep spaces, numbers, symbols unchanged
                result.append(char)

        return "".join(result)


def main():
    print("=== Caesar Cipher Encryption Tool ===")

    text = input("Enter your text: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    cipher = CaesarCipher(shift)

    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)

    print("\nEncrypted Text :", encrypted)
    print("Decrypted Text :", decrypted)


if __name__ == "__main__":
    main()