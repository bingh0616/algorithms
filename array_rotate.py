# right rotate array A by k
def rotate_array_right(A, k):
    k %= len(A)
    A = A[::-1]
    A = A[k-1::-1] + A[:k-1:-1]
    return A

# left rotate array A by k
def rotate_array_left(A, k):
    return rotate_array_right(A, len(A) - (k%len(A)))

def main():
    A = [1,2,3,6,7,8,9,4,5]
    print 'before:', A
    print 'after:', rotate_array_left(A, len(A)-1);

if __name__ == '__main__':
    main()

