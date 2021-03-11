from collections import Counter

def countOccurrencies(letter):
    return Counter(letter)

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text = ""
ngram_size = 3
chunks = [text[i:i+ngram_size] for i in range(0, len(text), ngram_size)]
print(countOccurrencies(chunks))