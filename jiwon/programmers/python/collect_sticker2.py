def solution(sticker):
    n = len(sticker)
    if n <= 2:
        return max(sticker)

    dp1, dp2 = [0] * n, [0] * n
    dp1[0], dp1[1] = sticker[0], sticker[1]
    dp2[1] = sticker[1]
    for i in range(1, n):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
    return max(dp1[-2], dp2[-1])
