import heapq
import time

class TimeBasedCache:
    def __init__(self):
        self.cache = {}
        self.expiry_heap = []
    
    def _cleanup(self):
        current_time = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            _, key = heapq.heappop(self.expiry_heap)
            if key in self.cache and self.cache[key][1] <= current_time:
                del self.cache[key]
    
    def set(self, key, value, expiryTime):
        self._cleanup()
        expiry_timestamp = time.time() + expiryTime
        self.cache[key] = (value, expiry_timestamp)
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))
    
    def get(self, key):
        self._cleanup()
        if key in self.cache:
            return self.cache[key][0]
        return None

    def user_choice(self):
        while True:
            print("1. Set a key-value pair with expiry")
            print("2.Display a value by key")
            print("3. Exit")
            choice = input("Enter the operation to be performed")
            if choice == "1":
                key = input("Enter key ")
                value = input("Enter value")
                expiryTime = int(input("Enter expiry time in seconds"))
                self.set(key, value, expiryTime)
            elif choice == "2":
                key = input("Enter key ")
                print("Value ", self.get(key))
            elif choice == "3":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    cache = TimeBasedCache()
    cache.user_choice()
