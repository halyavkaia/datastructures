from collections import deque
n = int(input())
target = ['white' if i % 2 == 0 else 'black' for i in range(n)]
dq = deque()
print ('Халявка Иван Андреевич 090301ПОВа-о24')
for i in range(n-1, -1, -1):
    if dq:
        dq.appendleft(dq.pop())
    dq.appendleft(target[i])
print(' '.join(dq))
