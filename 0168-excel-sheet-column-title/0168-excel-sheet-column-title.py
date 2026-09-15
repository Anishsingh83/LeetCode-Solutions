class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        title = []
        i = columnNumber
        while i > 26:
            j = i%26
            if j != 0:
                i = i//26
            else:
                i = i//26 - 1
            title.append(alph[j-1])
        title.append(alph[i-1])
        title.reverse()
        return ''.join(char for char in title)