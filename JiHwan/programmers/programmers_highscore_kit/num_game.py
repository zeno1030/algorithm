def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    for i in range(len(A)):
        if A[j] >= B[i]:
            pass
        else:
            answer += 1

    return answer