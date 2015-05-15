class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        for i in range(32):
            cnt += (n & 1)
            n >>= 1
        return cnt


def main():
    print Solution().hammingWeight(2)

if __name__ == '__main__':
    main()
