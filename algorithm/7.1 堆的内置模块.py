import heapq  # q -> queue  优先队列
import random

li = [i for i in range(100)]
random.shuffle(li)
print(li)

heapq.heapify(li)  # 键堆（小根堆）
print(li)

for i in range(len(li)):
    print(heapq.heappop(li), end='')  # heappop每次弹出最小的元素
