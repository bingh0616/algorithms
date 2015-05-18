# problem description: https://leetcode.com/problems/largest-number/

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        cmp = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        num = map(str, num)
        num = sorted(num, cmp)
        # manually remove the leading 0s because other language may not handle int(str) very good when str is very large
        return reduce(lambda a, b: str(int(a+b)), num[::-1])


def main():
    print Solution().largestNumber([0, 0])

if __name__ == '__main__':
    main()
