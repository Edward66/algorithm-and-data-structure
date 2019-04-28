def merge(li, low, mid, high):
    i = low
    j = mid + 1  # 第二段的第一个元素
    tmp_list = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            tmp_list.append(li[i])
            i += 1
        else:
            tmp_list.append(li[j])
            j += 1

    # while执行完，肯定有一段没数了。下面两个while肯定只执行一个
    while i <= mid:
        tmp_list.append(li[i])
        i += 1

    while j <= high:
        tmp_list.append(li[j])
        j += 1
    li[low:high + 1] = tmp_list


# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
# print(li)  # [1, 2, 3, 4, 5, 6, 7, 8]


def merge_sort(li, low, high):
    if low < high:  # 至少有两个，递归。 如果相等就只剩一个了
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        # 第一次跳到下面归并的时候肯定是上面两个遇到了递归终止条件。
        # 也就是长度为1的时候，这时候就把两个长度为1的，归并为长度为2的。然后栈开始往回走，直到归并完所有的。
        merge(li, low, mid, high)


li = list(range(100))
import random

random.shuffle(li)
merge_sort(li, 0, len(li) - 1)
print(li)
