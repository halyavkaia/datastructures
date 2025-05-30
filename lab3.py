from collections import deque
#Халявка Иван Андреевич#
n = int(input())
target = ['white' if i % 2 == 0 else 'black' for i in range(n)]
dq = deque()
for i in range(n-1, -1, -1):
    if dq:
        dq.appendleft(dq.pop())
    dq.appendleft(target[i])
print(' '.join(dq))
