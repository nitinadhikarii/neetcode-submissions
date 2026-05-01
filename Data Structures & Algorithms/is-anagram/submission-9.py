class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            dic={}
            for i in s:
                if i not in dic.keys():
                    dic[i]=1
                else:
                    dic[i]+=1
            dic1={}        
            for j in t:
                if j not in dic1.keys():
                    dic1[j]=1
                else:
                    dic1[j]+=1    
            if dic==dic1:
                return True
            else:
                return False
        else:
            return False                        

                