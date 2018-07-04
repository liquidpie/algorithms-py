'''
Count Possible Decodings of a given Digit Sequence

Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.

Examples:

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"

An empty digit sequence is considered to have one decoding.

https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

'''


def count_decodings(digits, n):
    '''
    Count possible decodings of a digit sequence
    
    :param digits: digits as char array
    :param n: size of array
    :return: int
    '''

    dp = [0] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):

        if digits[i - 1] > '0':
            dp[i] = dp[i - 1]

        if digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7'):
            dp[i] += dp[i - 2]

    return dp[n]
