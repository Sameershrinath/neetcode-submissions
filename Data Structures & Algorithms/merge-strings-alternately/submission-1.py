class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag=1
        ans=""
        i=0
        j=0
        while i<len(word1) and j< len(word2):
            if flag==1:
                ans=ans+word1[i]
                i+=1
                flag=2
            else:
                ans+=word2[j]
                j+=1
                flag=1
        while i<len(word1):
            ans+=word1[i]
            i+=1
        while j<len(word2):
            ans+=word2[j]
            j+=1

        return ans