def hanoi(n, a, b, c):  # 从a经过b移动到c
    if n > 0:
        # 因为n-1不是一块盘子，所以移动的过程肯定经过c了，但是不要去管怎么经过c的！
        hanoi(n - 1, a, c, b)  # 从a经过c移动到b
        print(f'moving from {a} to {c} ')
        # 同理,n-1不是一块，肯定要经过a，同样也不要去管怎么经过a的！
        hanoi(n - 1, b, a, c)  # 从a经过a移动到c


hanoi(64, 'A', 'B', 'C')
