class Solution:
    def addBinary(self, a: str, b: str) -> str:
        z = int(a,2) + int(b,2)
        out = str(bin(z)[2:])

        return out