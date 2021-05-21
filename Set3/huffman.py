from collections import Counter
import yaml

#Metodo di decodifica generico che prende in ingresso
#una stringa (codificata) ed un codebook (dizionario) e resitituisce
#la string decodificata
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


#Metodo di codifica generico che prende in ingresso
#una stringa ed un codebook (dizionario) e restituisce
#la stringa codificata
def encode(string,code):
    out = ""
    for word in string:
        out = out + code[word]
    return out


#Classe nodo per costruire l'albero (binario) di codifica
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0
        self.frequency = 0

    def children(self):
        return (self.left, self.right)

    def print_node(self):
        print(self.left, self.right, self.value,self.frequency)


#Metodo ricorsivo che prende in ingresso la radice dell'albero binario
#e costruisce i vari percorsi per raggiungere i caratteri dell'alfabeto.
#L'unico parametro del metodo è "root" che rappresenta la radici, gli altri
#due sono variabili d'appoggio per la ricorsione.
def huffman_tree(root,binString,d):
    if root.left == None or root.right==None:
        return binString
    left = root.left
    right = root.right
    c1 = huffman_tree(left,binString + "0",d)
    c2 = huffman_tree(right,binString + "1",d)
    if not isinstance(c1,list):
        d[left.value] = str(c1)
    if not isinstance(c2,list):
        d[right.value] = str(c2)
    return d


#Metodo che prende in ingresso una stringa, costruisce l'alfabeto
#l'albero e calcola i percorsi, restituisce il dizionario con la codifica
#di Huffman finale.
def huffman_buildCodebook(string):
    chars = Counter(string)
    nodes = []
    #Converto le parole in Nodi
    for item in chars:
        newnode = Node()
        newnode.value = item
        newnode.frequency = chars[item]
        nodes.append(newnode)


    #Costruisco l'albero con la regola vista
    #a lezione.
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency, reverse=False)
        n1 = nodes[0]
        n2 = nodes[1]
        del nodes[0]
        del nodes[0]
        n3 = Node()
        n3.left = n1
        n3.right = n2
        n3.value = ""
        n3.frequency = n1.frequency + n2.frequency
        nodes.append(n3)

    #calcolo i percorsi
    paths = huffman_tree(nodes[0],"",{})
    paths.pop("",None)
    return paths

#Metodo main
if __name__ == "__main__":
    in_ = input("Inserire stringa da codificare: ")
    codebook = huffman_buildCodebook(in_)
    print(yaml.dump(codebook)) #Per stampare il dizionario formattato.
    enc = encode(in_,codebook)
    dec = decode(enc,codebook)    
    print("Codificata: ", enc)
    print("Decodificata", dec)
