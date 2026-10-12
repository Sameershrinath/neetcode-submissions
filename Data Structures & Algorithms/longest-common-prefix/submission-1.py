class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        mini=1000
        for i in strs:
            if mini>len(i):
                mini=len(i)

        tempans=""

        j=0

        while j<mini:
            for i in strs:
                if tempans=="":
                    tempans=i[j]     
                if tempans!=i[j]:
                    tempans=""
                    break

            if tempans=="" and j == 0:
                return ""       
            if tempans=="":
                break
            result = result+ tempans
            tempans=""
            j=j+1
            

        return result
