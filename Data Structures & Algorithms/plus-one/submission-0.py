class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        m=[]
        for i in digits:
            s+=str(i)
        k=str(int(s)+1)
        for i in k:
            m.append((i))
        return m    
        
        
      
