class Solution(object):
    def isAnagram(self, s, t):
        char = [0] * 26
        for i in s:
            char[ord(i)-97] +=1
        for i in t:
            char[ord(i)-97] -=1
        for count in char:
            if count!=0:
                return False
        return True
    

# second solution

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)