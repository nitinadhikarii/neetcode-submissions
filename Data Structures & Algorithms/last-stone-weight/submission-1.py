class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
                x=max(stones)
                stones.remove(x)
                y=max(stones)
                stones.remove(y)
                if x==y:
                    pass
                else:
                    maxi=max(x,y)
                    mini=min(x,y)
                    stones.append(maxi-mini) 
        if len(stones)==0:
            return 0
        else:
            return stones[0]    
    



        