class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encode(self, st):
        ll = list(st.upper())
        actuall_list = [(self.alp[(self.alp.index(n)+self.shift)%26] if n in self.alp else n) for n in ll]
        # 這邊的寫法才對，因為要掉用變成index的只能是原先符號就是字母的，不然透過原先符號在self.alp找他的index會報錯，而且不用轉換成正數！負數就是倒著算
        aaa = ''.join(actuall_list)
        return aaa
        
    def decode(self, st):
        ll = list(st.upper())
        actuall_list = [(self.alp[(self.alp.index(n)-self.shift)%26] if n in self.alp else n) for n in ll]
        bbb = ''.join(actuall_list)
        return bbb

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encode(self, st):
        ll = list(st.upper())
        actuall_list = [
            self.alp[(self.alp.index(n) + self.shift) % 26] if n in self.alp else n
            for n in ll
        ]
        print(actuall_list)
        aaa = ''.join(actuall_list)
        return aaa
        
    def decode(self, st):
        ll = list(st.upper())
        actuall_list = [
            self.alp[(self.alp.index(n) - self.shift) % 26] if n in self.alp else n
            for n in ll
        ]
        bbb = ''.join(actuall_list)
        return bbb







c = CaesarCipher(5)
c.encode('codewar')
c.decode('BFKKQJX')

# c = CaesarCipher(5)
# print(c.encode('Codewars')) 'HTIJBFWX'
# print(c.decode('BFKKQJX'))  WAFFLES


# ll = ['a', 'b', 'c']
# print(ll[-1])