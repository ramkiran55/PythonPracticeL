"""

Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s.isnumeric():
            s=s[::-1]
        else:
            s1 = s[1:]
            s1 = s1[::-1]
            s = s[0]+s1
        if int(s) in range(-2**31, (2**31)-1):
            return int(s)
        else:
            return 0
    
x = int(input("please enter the number you want to reverse :"))
so = Solution()
print(so.reverse(x))
    