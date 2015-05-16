# problem description: https://leetcode.com/problems/simplify-path/

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        dirs = path.split('/')
        res = []
        for d in dirs:
            if d == '' or d == '.':
                continue
            elif d == '..':
                if res: res.pop()
            else:
                res.append(d)
        ret = '/'
        return ret + '/'.join(res)

def main():
    print Solution().simplifyPath('/..')

if __name__ == '__main__':
    main()
