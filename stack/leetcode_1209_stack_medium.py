"https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/"

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = [] # char, count
        for ch in s:
            if st and st[-1][0] == ch:
                st[-1][1] += 1
            else:
                st.append([ch, 1])
            if st[-1][1] == k:
                st.pop()
                
        result = ""
        for ch,count in st:
            result += ch*count
        return result
