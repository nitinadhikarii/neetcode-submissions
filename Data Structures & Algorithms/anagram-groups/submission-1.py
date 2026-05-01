class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        lis=[]
        for i in range(len(strs)):

            if tuple(sorted(strs[i])) not in hm.keys():
                hm[tuple(sorted(strs[i]))]=[strs[i]]
            else:    
                (hm[tuple(sorted(strs[i]))]).append(strs[i])

  
        for i in hm.keys():
            lis.append(hm[i])
        return lis      
        