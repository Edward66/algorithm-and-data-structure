import random

"""
堆排序
"""


# 大前提：节点的左右子树都是堆，但自身不是堆。
# 因为是从底部开始排序，所以每次向下调整的时候，下面的一定都是大根堆。
# 目的：通过一次向下调整将其变成一个堆。（不是放到最下面，是放到合适的位置,究竟放到拿，取决于堆顶的值）


def sift(li, top, bound):
    """
    top:  堆的根节点位置
    bound: 堆的最后一个元素的位置
    """
    i = top  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[top]  # 把堆顶存起来

    while j <= bound:  # 只要j位置有数（也就是i有节点），就一直循环
        # 左孩子和右孩子要先比较一下，大的放上去
        if j + 1 <= bound and li[j + 1] > li[j]:  # 右节点有并且比左节点大
            j = j + 1  # 跳到右边节点上。但是不能让这两个节点的值互换，因为不能保证左节点的值比右节点的子节点的值大

        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 把i放到当前节点
            j = 2 * i + 1  # i当前节点的左边的子节点
            # 在循环就是当前的i和他的子节点进行比较，如果子节点有比i大的，就把子节点放上去，把i放到刚刚放上去的子节点的位置。如果没有的话，那就退出循环，因为最一开始除了顶部节点，其他都是符合大根堆的，当前i的子节点没有比i大的，下面就更没有。
        else:  # tmp更大，也就是i找到了一个位置，这个位置的两个子节点都比i小，那么退出循环
            break
    li[i] = tmp  # 把i放到找到的位置

    """
    下面跳出循环的三种情况使用的都是这行代码：
    1: 当根节点（i,最开始的值）向下找，找到了合适自己的位置(根节点没有触底，此时下面已经没有比i大的值了)，那么跳出循环，把根节点的值（tmp，最开始堆顶的值）放到当前节点。(i跑中间了）
    2: 根节点找到最后了，下面没有值了，也就是所有的值都比根节点大，根节点触底了，也把根节点的值放到当前节点（原来的值已经
    上去了）  (i跑最后了)
    3: 当前节点一开始就比它的两个子节点大，当前节点的值还是等于当前节点。（i还是在一开始的位置）
    """


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)
    # 建堆完成了
    for i in range(n - 1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high


li = [i for i in range(100)]

random.shuffle(li)
print(li)

heap_sort(li)
print(li)
