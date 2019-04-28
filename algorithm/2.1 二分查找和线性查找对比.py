import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} running time:{t2 - t1} secs')
        return result

    return wrapper


@cal_time
def linear_search(li, val):
    for inx, v in enumerate(li):
        if v == val:
            return inx

    else:
        return None


@cal_time
def binary_search(li, item):
    left = 0
    right = len(li) - 1

    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == item:
            return mid
        elif li[mid] > item:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid] < item  待查找的值在mid右侧
            left = mid + 1


li = list(range(100000000))
linear_search(li, 50000000)  # linear_search running time:4.583159923553467 secs
binary_search(li, 50000000)  # binary_search running time:3.0994415283203125e-05 secs  注意是-05
