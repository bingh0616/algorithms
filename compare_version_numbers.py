# problem description: https://leetcode.com/problems/compare-version-numbers/

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            val1, val2 = 0, 0
            if i < len(v1): val1 = int(v1[i])
            if j < len(v2): val2 = int(v2[j])
            i += 1
            j += 1
            if val1 != val2:
                return 1 if val1 > val2 else -1
                
        return 0

def main():
    print Solution().compareVersion('1.0', '1')

if __name__ == '__main__':
    main()
