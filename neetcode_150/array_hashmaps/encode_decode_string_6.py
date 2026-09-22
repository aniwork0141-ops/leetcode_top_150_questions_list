def encode(strs):
    encoded_string = ""
    for char in strs:
        encoded_string += str(len(char))+"#"+char
    return encoded_string

def decode(s):
    decoded_string = []
    i = 0 #pointer 1 to track complete combination i.e Number+#+Word
    while i < len(s):
        j = i #pointer 2 to iterate over each character
        while s[j] != "#":
            j+=1 #this gives me the length of the upcoming adjacent word
        length = int(s[i:j])
        decoded_string.append(s[j+1:j+1+length])
        i = j+1+length #pointer 1 moves to next combination i.e Number+#+Word
    return decoded_string

