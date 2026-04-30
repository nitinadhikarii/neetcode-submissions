class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s[::-1]
        s2=''
        s3=''
        for i in ((s)):
            if i.isalnum():
                s2+=(i.lower())
        for i in s1:
            if i.isalnum():
                s3+=(i.lower())        
                
        return s2  ==s3   
