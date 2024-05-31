class CaesarCipher(object):
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        print("Shift value:", self.shift)  # This will print the shift value
        ll = list(st.upper())
        return ll
        
    def decode(self, st):
        pass

alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def encode(st):
    ll = list(st.upper())
    return ll

print(encode('Codewars'))

# c = CaesarCipher(5)
# print(c.encode('Codewars'))
# print(c.decode('BFKKQJX'))