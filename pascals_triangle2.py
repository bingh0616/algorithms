class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        prev = [1] * (rowIndex+1)
        
        for i in range(2, rowIndex+1):
            curr = [1] * (rowIndex+1)
            for j in range(1, i):
                curr[j] = prev[j-1] + prev[j]
            prev = curr
            
        return prev
            
def main():
    print Solution().getRow(3)

if __name__ == '__main__':
    main()
