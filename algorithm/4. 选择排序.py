def select_sort(li):
    for i in range(len(li) - 1):  # i是第几趟
        min_log = i  # 无序区最小数的位置
        for j in range(i + 1, len(li)):  # 遍历无序区，自己不用和自己比
            if li[j] < li[min_log]:
                min_log = j
        li[i], li[min_log] = li[min_log], li[i]


li = [3, 4, 12, 551, 331, 11, 34]
select_sort(li)
print(li)
