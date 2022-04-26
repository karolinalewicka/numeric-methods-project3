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

def divide_occurences(occurences):
    buffer = []
    for number in occurences:
        if number > 255:
            while number > 255:
                number -= 255
                buffer.append(255)
                buffer.append(0)
        buffer.append(number)
    return buffer

assert divide_occurences([300, 400]) == [255, 0, 45, 255, 0, 145]  



def rle_coding(binary_stream):
    occurences = get_occurences(binary_stream)
    return divide_occurences(occurences)


              

assert rle_coding("011000") == [1, 2, 3]
assert rle_coding(convert_to_binary_stream("AB")) == [1, 1, 5, 1, 1, 1, 4, 1, 1]
assert rle_coding("1" * 1023 + "000001") == [255, 0, 255, 0, 255, 0, 255, 0, 3, 5, 1] # 1023 => 255 0 255 0 255 0 255 0 3 