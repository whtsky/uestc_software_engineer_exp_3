score_sum = 0
count = 0
useful_count = 0
while count < 50:  # 1
    n = int(input('输入一个数:')) # 2
    if n == -1:  # 3
        break
    count += 1  # 4
    if 0 <= n <= 100: # 5
        useful_count += 1
        score_sum += n # 6
# Q: while/else 的流程图该怎么画？
else:
    print('输入太多了。') # 7
    exit()

print("有效分数有%d个，总分为%d，平均值为%d" % (
    useful_count, score_sum, useful_count and score_sum/useful_count or 0
)) # 8

#9: end
