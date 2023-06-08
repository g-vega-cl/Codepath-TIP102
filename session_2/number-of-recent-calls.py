from collections import deque
import unittest


class RecentCounter:

    def __init__(self):
        # Create a new queue
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Upon Ping add new ping to queue
        self.queue.append(t)

        # Remove all ping in queue with value more than 3000 away from new ping
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()
        
        # Return length of queue
        return len(self.queue)
    
class RecentCounterTest(unittest.TestCase):
    def test_recent_counter_example_case(self):
        recentCounter = RecentCounter()
        self.assertEqual(recentCounter.ping(1),1)
        self.assertEqual(recentCounter.ping(100), 2)
        self.assertEqual(recentCounter.ping(3001), 3)
        self.assertEqual(recentCounter.ping(3002), 3)

    def test_recent_counter_edge_case(self):
        recentCounter = RecentCounter()
        self.assertEqual(recentCounter.ping(1),1)
        self.assertEqual(recentCounter.ping(100), 2)
        self.assertEqual(recentCounter.ping(300), 3)
        self.assertEqual(recentCounter.ping(400), 4)
        self.assertEqual(recentCounter.ping(4000), 1)

    def test_recent_counter_single_ping(self):
        recentCounter = RecentCounter()
        self.assertEqual(recentCounter.ping(1),1)
        self.assertEqual(recentCounter.ping(2), 2)

if __name__ == '__main__':
    unittest.main()



# Solution using functions
def recent_counter(pings):
    queue = deque()
    result = []
    for t in pings:
        queue.append(t)
        while queue and queue[0] + 3000 < t:
            queue.popleft()
        result.append(len(queue))
    return result


# Example cases
pings1 = [1, 100, 3001, 3002]
print(recent_counter(pings1))  # Output: [1, 2, 3, 3]

pings2 = [1, 100, 300, 400, 4000]
print(recent_counter(pings2))  # Output: [1, 2, 3, 4, 1]

# Edge case
pings3 = [1]
print(recent_counter(pings3))  # Output: [1]