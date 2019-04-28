import random


def bucket_sort(li, n=100, max_num=1000):
    """
    :param li: 列表
    :param n: 桶数
    :param max_num: 最大数
    :return:
    """
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        # i 表示var放到几号桶里。
        i = min(var // (max_num // n), n - 1)  # 最大的是99号桶，取最小值，也就是只要超过99的，最后取出来都是99的
        buckets[i].append(var)  # 把bar加到桶里面

        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):  # 从最后一个开始和前面的比较，到第二个元素停
            if buckets[i][j] < buckets[i][j - 1]:  # [0,2,4,1] 如，1和4交换，然后和2交换，最后成为[0,1,2,4]
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for bucket in buckets:
        sorted_li.extend(bucket)

    return sorted_li


li = [random.randint(0, 1000) for i in range(10000)]
# print(li)
li = bucket_sort(li)
print(li)
