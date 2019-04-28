import random


def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        exchange = False
        for j in range(len(li) - i - 1):  # 箭头，比如i是9，最多挪8次，就把9挪到最右边了。
            if li[j] > li[j + 1]:  # 换成小于号就是降序
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


# li = [random.randint(0, 10000) for i in range(1000)]
# bubble_sort(li)
# print(li)

li = [7, 2, 4, 6, 5, 1, 8, 9, 3]
print('原列表', li)
bubble_sort(li)
