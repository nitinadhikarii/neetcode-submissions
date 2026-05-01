class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        lis=[]
        for i in range(len(strs)):

            if ("".join(sorted(strs[i]))) not in hm.keys():
                hm["".join(sorted(strs[i]))]=[strs[i]]
            else:    
                (hm["".join(sorted(strs[i]))]).append(strs[i])

  
        for i in hm.keys():
            lis.append(hm[i])
        return lis        

