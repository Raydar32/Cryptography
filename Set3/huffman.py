from collections import Counter

def decode(string,code):
    r_code = {value : key for (key, value) in code.items()}
    out = ""
    buffer = ""
    for word in string:
        buffer = buffer + word
        if buffer in r_code:
            out = out + r_code[buffer]
            buffer = ""
    return out
            
        
def encode(string,code):
    out = ""
    for word in string:
        out = out + code[word]
    return out
        

alpha = ["a","b","c","d"]
code = {
        "a" : "11",
        "b" : "10",
        "c" : "01",
        "d" : "00"}

string = "abcabcabcabcabcbbcccabcabcdadadadadad"

enc = encode(string,code)
dec = decode(enc,code)
res = Counter(string)
