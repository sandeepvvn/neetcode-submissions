class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_list= sorted(list(s))
            t_list= sorted(list(t))

            if s_list == t_list:
                return True
        
        return False