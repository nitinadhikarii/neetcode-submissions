class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p=[]
        for i in numbers:
            for j in numbers:
                if i+j == target and i<j and i!=j:
                    p.append([numbers.index(i)+1,numbers.index(j)+1])
                    break
        return p[0]                        