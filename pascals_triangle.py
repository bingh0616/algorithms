class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        res = [[1] * (i+1) for i in xrange(numRows)]
        for i in xrange(2, numRows):
            for j in xrange(1, i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
                
        return res

def main():
    print Solution().generate(3)

if __name__ == '__main__':
    main()
