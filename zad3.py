def ascii_value(num):
    return ord(num)

def letter_to_binary(letter):
    n = ord(letter)
    array = []
    while n > 0:
        array.insert(0, str(n%2))
        n = n // 2
    txt =  "".join(array)
    txt = '0' * (8 - len(txt)) + txt
    return txt


def convert_to_binary_stream(text):
    return "".join([letter_to_binary(char) for char in text])


assert convert_to_binary_stream("AB") == "0100000101000010" 

def get_occurences(stream):
    output = []
    counter = 1
    
    for i in range(0, len(stream) - 1):
        current_character = stream[i]
        next_character = stream[i+ 1]
        if current_character == next_character:
            counter += 1
        else:
            output.append(counter)
            counter = 1
    output.append(counter)
    return output

def divide_occurences(occurences, bits):
    buffer = []
    value = 2 ** bits - 1
    for number in occurences:
        if number > value:
            while number > value:
                number -= value
                buffer.append(value)
                buffer.append(0)
        buffer.append(number)
    return buffer

assert divide_occurences([700, 800], 9) == [511, 0, 189, 511, 0, 289]  

def decimal_to_binary(n, bits=8):
    array = []
    while n > 0:
        array.insert(0, str(n%2))
        n = n // 2
    bin = "".join(array)
    bin =  '0' * (bits - len(bin)) + bin
    return bin


def encode_bits(array, bits):
    return "".join([decimal_to_binary(number, bits) for number in array])

assert encode_bits([10, 15], 5) == "01010" + "01111"

def encode_rle(array, bits):
    stream = encode_bits(array, bits)

    buffer = ""
    buffer += decimal_to_binary(bits)

    remaining = 8 - (len(array) * bits - 5) % 8
    buffer += decimal_to_binary(remaining, bits=3)
    temp, stream = stream[:5], stream[5:]
    buffer += temp

    while len(stream) > 8:
        temp, stream = stream[:8], stream[8:]
        buffer += temp

    buffer += stream
    buffer += "0" * remaining

    return buffer

assert encode_rle([511, 0, 10], 9) == "00001001" + ("010" + "1" * 5) + ("1" * 4 + "0" * 4) + ("0" * 5 + "0" * 3) + ("0" * 2 + "1010" + "0" * 2)
# 8 bits - n
# 8 bits - 3 bits R + 5 bits encode (22 left out of 27)
# 2 * 8 bits (6 left)
# 8 - 6 bits to encode and 2 remaining bits

