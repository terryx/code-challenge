# Write a function that takes a string as input and returns the string reversed. 
class Solution:
    def reverseString(self, s: str) -> str:
        arr = list(s)
        left = 0
        right = len(arr) - 1
       
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1 

        return ''.join(arr)

class TestSolution:
    def test_reverseStrings(self):
        solution = Solution()
        ans = solution.reverseString('hello')
        assert ans == 'olleh'
