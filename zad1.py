
def ascii_value(num):
    return ord(num)

assert ascii_value("P") == 80 # +2
assert ascii_value("I") == 73 # +21
assert ascii_value("E") == 69 # +17
assert ascii_value("S") == 83 # +5

def is_upper(letter):
    return 65 <= ascii_value(letter) <= 90

assert is_upper("A")

def is_lower(letter):
    return 97 <= ascii_value(letter) <= 122

assert is_lower("a")

def is_above_upper_limit(value):
    return value > 90

assert is_above_upper_limit(91)

def is_above_lower_limit(value):
    return value > 122

assert is_above_lower_limit(123)

def transpose(letter, cipher):
    if letter == " ":
        return letter
    offset = ascii_value(cipher) % 26
    number = ascii_value(letter)
    ciphered_number = number + offset
    if (is_lower(letter) and is_above_lower_limit(ciphered_number)) or (
        is_upper(letter) and is_above_upper_limit(ciphered_number)
    ):
        ciphered_number -= 26
    return chr(ciphered_number)


assert transpose("A", "P") == "C"
assert transpose(" ", "X") == " "
assert transpose("Z", "P") == "B"

def transposition_cipher(text, key):
    output = ""
    spaces = 0
    for index, char in enumerate(text):
        if char == " ":
            spaces += 1
        output += transpose(char, key[(index - spaces) % len(key)])
    return output

assert transposition_cipher("ALA MA KOTA", "PIES") == "CGR RC FFYC"
assert transposition_cipher("ala ma kota", "PIES") == "cgr rc ffyc"
