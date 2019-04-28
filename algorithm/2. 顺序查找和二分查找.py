# 顺序查找

def linear_search(li, val):
    for inx, v in enumerate(li):
        if v == val:
            return inx

    else:
        return None


# 二分查找


def binary_search(li, item):
    left = 0
    right = len(li) - 1

    while left <= right:  # 候选区有值
        mid = int(left + right) // 2
        if li[mid] == item:
            return mid
        elif li[mid] > item:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid] < item  待查找的值在mid右侧
            left = mid + 1


li = list(range(100000000))
print(binary_search(li, 50000000))
