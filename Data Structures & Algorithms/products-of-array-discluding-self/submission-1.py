class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i = 0 
        # ans=[]

        # while i<len(nums):
        #     multi=1
        #     j=0
        #     while j<len(nums):
        #         if i==j:
        #             j+=1
        #             continue
        #         multi=multi*nums[j]
        #         j+=1
        #     ans.append(multi)
        #     i+=1
        # return ans 
        ans=[]
        multi=1
        totalzero=0
        for i in nums:
            if i!=0:
                multi=multi*i
            else:
                totalzero+=1
        if totalzero > 1:
            for i in nums:
                ans.append(0)
            return ans
        elif totalzero == 1:
            for i in nums:
                if i ==0:
                    ans.append(multi)
                else:
                    ans.append(0)
            return ans
        else:
            for i in nums:
                ans.append(multi//i)
            return ans
        return ans
        
