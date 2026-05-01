class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        lis=[]
        for i in range(len(strs)):

            if ("".join(sorted(strs[i]))) not in hm.keys():
                hm["".join(sorted(strs[i]))]=[strs[i]]
            else:    
                (hm["".join(sorted(strs[i]))]).append(strs[i])

        # for i in range(len(hm)):
        #     for j in range(len(hm)):
        #         if hm[i]==hm[j] and strs[i]!=strs[j]:
        #             if [strs[i],strs[j]] not in lis:
        #                 lis.append([strs[i],strs[j]])
        # return lis   
        for i in hm.keys():
            lis.append(hm[i])
        return lis        



        