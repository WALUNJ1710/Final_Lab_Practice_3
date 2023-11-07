def knapsack(W, wt, val, n):
    K = [[0] * (W + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Find the selected items (both 0-based and 1-based indices)
    selected_items_0_based = []
    selected_items_1_based = []
    i, w = n, W
    while i > 0 and w > 0:
        if K[i][w] != K[i - 1][w]:
            selected_items_0_based.append(i - 1)
            selected_items_1_based.append(i)
            w -= wt[i - 1]
        i -= 1
    selected_items_0_based.reverse()
    selected_items_1_based.reverse()

    return K[n][W], selected_items_0_based, selected_items_1_based

val = [60, 100, 120,150]
wt = [10, 20, 30,50]
W = 70
ln = len(val)
profit, selected_items_0_based, selected_items_1_based = knapsack(W, wt, val, ln)

print("Maximum Profit achieved with this knapsack: ", profit)
print("Selected items (0-based indices):", selected_items_0_based)
print("Selected items (1-based indices):", selected_items_1_based)
