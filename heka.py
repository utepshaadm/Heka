''' Heka Card Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class HEKA:
    def __init__(self):
        self.deck = list(range(52))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def step(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         self.deck.insert(self.deck[1], self.deck.pop(0))
         
    def encrypt_letter(self, letter):
        self.step()
        num = ord(letter) - 65
        key = self.deck[self.deck[0]] % 26
        num = (num + key) % 26
        return chr(num + 65)
        
    def decrypt_letter(self, letter):
        self.step()
        num = ord(letter) - 65
        key = self.deck[self.deck[0]] % 26
        num = (num - key)
        return chr(num + 65)

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
        
heka = HEKA()
heka.gen_rand_decks()
msg = "HELLOWORLD"
ctxt = heka.encrypt(msg)
print(ctxt)
