# 所有这些排序都可以叫比较排序
def sift(li, top, bound):
    """
    top:  堆的根节点位置
    bound: 堆的最后一个元素的位置
    """
    i = top
    j = 2 * i + 1
    tmp = li[top]

    while j <= bound:
        # 建立一个小根堆
        if j + 1 <= bound and li[j + 1] < li[j]:
            j = j + 1

        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    # 1. 建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)

    # 2. 把大于堆顶的数放到顶部，然后重新建堆

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    # 3. 遍历,选出最大的10个
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)  # 保证从大倒小按降序排列

    # 3. 出数
    return heap


import random

li = list(range(100))
random.shuffle(li)
print(topk(li, 19))
