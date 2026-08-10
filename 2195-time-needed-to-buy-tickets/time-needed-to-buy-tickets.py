class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        from collections import deque
        queue = deque()
        for i in range(len(tickets)):
            queue.append((i, tickets[i]))
        time = 0
        while len(queue) > 0:
            person, tickets = queue.popleft()
            tickets -= 1
            time += 1
            if person == k and tickets == 0:
                return time
            if tickets > 0:
                queue.append((person, tickets))
