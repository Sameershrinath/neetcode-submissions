class Solution:
    def __init__(self):
        self.newstring=""

    def encode(self, strs: List[str]) -> str:
        if strs:
            for i in strs:
                self.newstring=self.newstring+i+"/$"
        return self.newstring

    def decode(self, s: str) -> List[str]:
        if len(self.newstring)>0:
            return self.newstring.split("/$")[:len(self.newstring.split("/$"))-1]
        else:
            return []
