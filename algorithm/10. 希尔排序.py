def insert_sort_gap(li, gap):  # gap就是分的组
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap  # 原来是看前面那张牌，现在不是了，是看前d张牌
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    gap = len(li) // 2
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap //= 2


import random

li = [i for i in range(100)]
random.shuffle(li)
shell_sort(li)
