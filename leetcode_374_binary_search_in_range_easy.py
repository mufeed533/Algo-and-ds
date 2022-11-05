"https://leetcode.com/problems/guess-number-higher-or-lower/submissions/837232772/"

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n

        curr = 1

        while curr <= n:
            mid = (s+e) // 2
            
            is_guess_correct = guess(mid)
            if is_guess_correct == 0:
                return mid
            elif is_guess_correct == -1:
                e = mid -1
            else:
                s = mid + 1
            curr += 1
