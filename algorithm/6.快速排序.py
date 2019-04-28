# def quicksort(array):
#     if len(array) < 2:
#         return array
#
#     pivot = array[0]
#
#     lesser = [item for item in array[1:] if item <= pivot]
#     greater = [item for item in array[1:] if item > pivot]
#
#     return quicksort(lesser) + [pivot] + quicksort(greater)


#
#
# print(quicksort([5, 10, 23, 222, 55, 3, 0, 55, 12, 412, 4]))

def partition(array, left, right):
    pivot = array[left]
    while left < right:
        #  当右边没有比pivot小的数，right就一直走到和left重合了，下面这个条件是无法退出循环的,right会一直-1
        # while array[right] >= pivot:
        while left < right and array[right] >= pivot:  # 从右边找比pivot小或等于pivot的数
            right -= 1  # 往左走一步
        # 如果left已经和right重合了。那么array[left]=array[right]就是自己等于自己
        array[left] = array[right]  # 找到了比pivot小的数，把当前小的那个数放到最左边

        # 下面的while的left<right有两个作用：
        # 1. 在上一个while循环的时候就可能找到了left = right了
        # 2. 在自己while循环的过程中left=right了
        while left < right and array[left] <= pivot:  # 左边找比pivot大或等于pivot的数
            left += 1
        # 因为上面的right一直在往左移动，所以array[right]的位置是往左移动完的位置，并且它的值已经放到最左边了。
        # 或者是和left重合的位置，这样array[right]=array[left]就是自己等于自己
        array[right] = array[left]  # 把左边的值写到右边空位上

    array[left] = pivot  # array[left]和array[right]相等了（也就是在中间了），把原来的值放回中间
    return left  # left和right都行，最后left和right碰上了


# left和right代表最左边和最右边的值
def quick_sort(array, left, right):
    if left < right:  # left = right 就一个元素， left小于right至少有两个元素
        mid = partition(array, left, right)
        quick_sort(array, left, mid - 1)
        quick_sort(array, mid + 1, right)


li = [5, 7, 4, 6, 3, 3, 1, 2, 9, 8]
quick_sort(li, 0, len(li) - 1)
print(li)
