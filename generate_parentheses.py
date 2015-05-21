# problem description: https://leetcode.com/problems/generate-parentheses/

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        solution = ''
        res = []
        self.helper(n, n, solution, res)
        return res
    
    def helper(self, left, right, solution, res):
        if left == right == 0:
            res.append(solution[:])
        elif left >= right:
            solution += '('
            self.helper(left-1, right, solution, res)
        else:
            solution += '('
            if left > 0: self.helper(left-1, right, solution, res)
            solution = solution[:-1] + ')'
            if right > 0: self.helper(left, right-1, solution, res)


def main():
    print Solution().generateParenthesis(3)

if __name__ == '__main__':
    main()
