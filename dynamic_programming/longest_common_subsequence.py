def longest_common_subsequence(seq1, seq2):
    """
        Given two sequences, find the length of longest subsequence present in both of them. 
        A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    :param seq1: first sequence 
    :param seq2: second sequence
    :return: length of the longest common sequence
    """

    m = len(seq1)
    n = len(seq2)
    lcs = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    print_lcs(seq1, seq2, lcs)

    return lcs[m][n]


def print_lcs(seq1, seq2, lcs):
    i, j = len(seq1), len(seq2)

    common_subseq = []
    while i > 0 and j > 0:
        # If current character in seq1 and seq2 are same, then
        # current character is part of LCS
        if seq1[i - 1] == seq2[j - 1]:
            common_subseq.append(seq1[i - 1])
            i -= 1
            j -= 1
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(' '.join([str(x) for x in common_subseq[::-1]]))


if __name__ == '__main__':
    seq1 = "AGGTAB"
    seq2 = "GXTXAYB"

    print(longest_common_subsequence(seq1, seq2))