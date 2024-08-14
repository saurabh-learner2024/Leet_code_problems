from collections import deque

dq = deque(["Red", "Green", "White"])


def dequeue_problem():
    dq.appendleft("Pink")
    dq.append("Pink")
    dq.pop()
    dq.popleft()
    dq.reverse()
    return dq


print(dequeue_problem())
