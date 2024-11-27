#Complex exercise
import os
class Cypher:
    _abc_lower = 'abcdefghijklmnopqrstuvwxyz'
    _abc_upper = 'ABCDEFJHIJKLMNOPQRSTUVWXYZ'

    def encrypt_text(self, text):
        pass

    def decrypt_text(self, text):
        pass

    def encrypt_filename(self, filename):
        pass

    def decrypt_filename(self, filename):
        pass

    def crack(self, text):
        pass

    

class Ceaser(Cypher):
    def __init__(self, shift):
        self._shift = shift

    def encrypt_text(self, text):
        result = ''
        for i in text:
            if i in Cypher._abc_lower:
                index = (Cypher._abc_lower.find(i) + self._shift)%26
                result = result + Cypher._abc_lower[index]
            elif i in Cypher._abc_upper:
                index = (Cypher._abc_upper.find(i) + self._shift)%26
                result = result + Cypher._abc_upper[index]
            else:
                result += i
        return result
    
    def decrypt_text(self, text):
        result = ''
        for i in text:
            if i in Cypher._abc_lower:
                index = (Cypher._abc_lower.find(i) - self._shift)%26
                result = result + Cypher._abc_lower[index]
            elif i in Cypher._abc_upper:
                index = (Cypher._abc_upper.find(i) - self._shift)%26
                result = result + Cypher._abc_upper[index]
            else:
                result += i
        return result

    def crack(self, text):
        self._shift = 0
        shift = 0
        print(self.decrypt_text(text))
        ch = input('Is it OK? ')
        while shift < 26 and ch != 'y':
            shift += 1
            u = Ceaser(shift)
            print(u.decrypt_text(text))
            ch = input('Is it OK? ')
        if ch == 'y':
            print('The text has been decrypted', shift)

    def __str__(self):
        return f'{self}'
    
    def encrypt_file(self, filename):
        text = []
        with open(filename) as f:
            text = f.readlines()
        for i in range(len(text)):
            encrypted = self.encrypt_text(text[i])
            text[i] = encrypted
        with open(filename, 'w') as f:
            for i in text:
                f.write(i)
                
    def decrypt_file(self, filename):
        text = []
        with open(filename) as f:
            text = f.readlines()
        for i in range(len(text)):
            decrypted = self.decrypt_text(text[i])
            text[i] = decrypted
        with open(filename, 'w') as f:
            for i in text:
                f.write(i)

class Riddle(Ceaser):
    _plaintext = ''
    _chypertext = ''

    def __init__(self, plainfile, chyperfile, decode = None):
        self._plaintext = plainfile
        self._chypertext = chyperfile
        if decode !=None:
            self._decode = decode
        with open(plainfile) as f:
            Riddle._plaintext = f.read().upper()
        with open(chyperfile) as g:
            Riddle._chypertext = g.read().upper()

    def sort_freq(self, text):
        d = {}
        for c in text:
            if c in d.keys() and c in Cypher._abc_upper:
                d[c] += 1
            elif c in Cypher._abc_upper:
                d[c] = 1
        l = list(d.items())
        for i in range(len(l)-1):
            for j in range(len(l)-i):
                if l[j][1] > l[j+1][1]:
                    l[j], l[j+1] = l[j + 1], l[j]





text = Ceaser(3)
message = text.encrypt_text('Hello World')
print(message)
print(text.decrypt_text(message))
#text.crack(message)

#text.encrypt_file('plaintext.txt')
#text.decrypt_file('plaintext.txt')

r = Riddle('plaintext.txt', 'ciphertext.txt')


