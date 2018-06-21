'''

Find Nth fibonacci number in O(logN) time complexity.

Solution: 

We all know the Fibonacci recurrence as F(n+1) = F(n) + F(n-1) but we can represent this in the form a matrix as shown below:

       | 1  1 |   *   |   f(n)  |    =    | f(n + 1) |
       | 1  0 |       | f(n - 1)|         |   f(n)   |


Look at the matrix A = [ [ 1 1 ] [ 1 0 ] ] . Multiplying A with [ F(n) F(n-1) ] gives us [ F(n+1) F(n) ] , so we say that

A* [ F(n) F(n-1) ] = [ F(n+1) F(n) ]

start with [ F(1) F(0) ] , multiplying it with A gives us [ F(2) F(1) ]; again multiplying [ F(2) F(1) ] with A gives us [ F(3) F(2) ] and so on...

    A* [ F(1) F(0) ] = [ F(2) F(1) ]
    A* [ F(2) F(1) ] = [ F(3) F(2) ] = A^2 * [ F(1) F(0) ]
    A* [ F(3) F(2) ] = [ F(4) F(3) ] = A^3 * [ F(1) F(0) ]
    ..
    ..
    ..
    ..
    A* [ F(n) F(n-1) ] = [ F(n+1) F(n) ] = A^n * [ F(1) F(0) ]


So all that is left is finding the nth power of the matrix A. Well, this can be computed in O(log n) time, by recursive doubling. The idea is, to find A^n , we can do R = A^(n/2) * A^(n/2) and if n is odd, we need do multiply with an A at the end. The following pseudo code shows the same.

    Matrix findNthPower( Matrix M , power n ) :
        if n == 1: 
            return M
            
        Matrix R = findNthPower ( M , n/2 )
        R = RxR # matrix multiplication
        if n % 2 == 1:
            R = R x M # matrix multiplication
        return R
        

In this manner, by using the magic of DP, we can get the Nth fibonacci number in O(logN).

'''


def find_nth_power(matrix, n):
    if n == 1:
        return matrix

    res = find_nth_power(matrix, n // 2)
    res = res * res

    if n % 2 == 1:
        res = matrix * res

    return res
