import copy
import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


def partition(array, left, right):
    pivot = array[left]
    while left < right:
        while left < right and array[right] >= pivot:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= pivot:
            left += 1
        array[right] = array[left]

    array[left] = pivot
    return left


def _quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        _quick_sort(array, left, mid - 1)
        _quick_sort(array, mid + 1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


@cal_time
def radix_sort(li):
    max_num = max(li)
    iteration = 0
    while 10 ** iteration <= max_num:  # 1 10 100 1000 10000 ......
        buckets = [[] for _ in range(10)]  # 桶的数量是固定的，0-9

        # 分桶
        for val in li:
            # 987 取7：987 % 10 -> 7（987 // 1 % 10）。 取8：987 // 10 % 10 -> 8。取9：987 // 100 % 10
            digit = (val // 10 ** iteration) % 10
            buckets[digit].append(val)

        li.clear()

        # 把数重新写回li
        for bucket in buckets:
            li.extend(bucket)

        # 基数排序是从个位开始装了多次桶，桶内并没有排序的过程

        iteration += 1


li = [random.randint(0, 10000) for _ in range(100000)]
random.shuffle(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)  # nlogn logn = log(2,n)  # 0.33087706565856934
radix_sort(li2)  # kn = log(10,n)  # 0.17744874954223633

# 随着random.randint(0, 10000)随机数增加，基数排序就会慢下来，不如快速排序快。
print(li2)
