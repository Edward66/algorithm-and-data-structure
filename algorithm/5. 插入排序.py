import random
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
def insert_sort(li):
    for i in range(1, len(li)):  # i 表示已经刚摸到的牌的下标
        tmp = li[i]  # 摸到的牌
        j = i - 1  # j指的是手里已经有的牌的下标

        # while循环是找插入的位置
        while j >= 0 and li[j] > tmp:  # j等于-1说明没有牌了。这张牌要比我手里的牌大
            li[j + 1] = li[j]  # 手里已有的牌比摸到的牌大，往右挪一个 -->比如手里拿的是9，tmp是8，9比8大，就挪到8的右边
            j -= 1  # j的箭头在往左移一个
        li[j + 1] = tmp  # while循环结束后，把刚摸到的牌，放到j前面。因为while循环完后的tmp（摸到的牌），肯定是比j（手上的牌）大的。


li = list(range(10000))
random.shuffle(li)
insert_sort(li)
