import copy
import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f'{func.__name__} run time is', time.time() - start)

    return wrapper


@cal_time
def count_sort(li, max_count=100):
    """
    :param li:
    :param max_count: 最大的那个数
    :return:
    """
    count = [0 for _ in range(max_count + 1)]  # 如果最大值是100，列表长度需要是101（加上0)
    for val in li:
        count[val] += 1  # 找到一个就加1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):  # val记录了每个数出现了几次
            li.append(ind)  # 比如0出现了8次，那么就循环增加8个0


@cal_time
def sys_sort(li):
    li.sort()


li = [random.randint(0, 100) for _ in range(1000)]

# li1 = copy.deepcopy(li)
# li2 = copy.deepcopy(li)
#
# count_sort(li1)  # count_sort run time is 1.2575359344482422
# sys_sort(li2)  # sys_sort run time is 1.0089600086212158
count_sort(li)
print(li)
