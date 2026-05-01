class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test = min(strs)          
        lcp = ""
        strs.remove(min(strs))    

        for i in range(len(test)):
            for j in strs:
                if test[i] != j[i]:  
                    return lcp
            lcp += test[i]           

        return lcp