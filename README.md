Features Implemented

1. MinMaxStack

A stack data structure with O(1) operations for:

push(x): Adds an element to the stack.

pop(): Removes the top element.

top(): Retrieves the top element without removing it.

getMin(): Returns the smallest element in the stack.

getMax(): Returns the largest element in the stack.

Interactive menu for user-driven execution.

2. Interval Merger

Maintains a set of non-overlapping intervals.

Operations:

addInterval(start, end): Adds an interval and merges overlapping ones.

getIntervals(): Retrieves merged intervals.

Interactive menu for adding intervals dynamically and viewing the results.

3. Time-Based Cache

Implements a key-value cache with expiry support.

Operations:

set(key, value, expiryTime): Stores a key-value pair with an expiration time.

get(key): Retrieves a value if it exists and hasn't expired.

Automatic cleanup of expired keys.

Interactive menu for setting and retrieving key-value pairs.

Technologies Used

Python: The entire implementation is done in Python.

Data Structures Used:

Stack for MinMaxStack.

Sorted list with merging for Interval Merger.

Dictionary and heap for Time-Based Cache.

Heapq Library: Used for maintaining expiry time in Time-Based Cache.



Setup Instructions

Install Python 

Clone or Download the Code

Run Each Program Separately

Open a terminal or command prompt.

Navigate to the directory containing the program.

Run the script using:

python filename.py

Follow the on-screen menu to interact with the program.



Implementation Details

1.MinMaxStack

Uses a main stack for storing elements.

Maintains two auxiliary stacks:

min_stack to track the minimum element.

max_stack to track the maximum element.

Operations are O(1) for push, pop, and retrieval.

2.Interval Merger

Stores intervals in a sorted list.

On insertion, merges overlapping intervals to maintain a non-overlapping set.

Sorting ensures efficient merging, leading to O(log n) insertion time.

3.Time-Based Cache

Uses a dictionary to store key-value pairs with expiry timestamps.

Maintains a min-heap for efficient expiry tracking.

Automatic cleanup ensures expired keys are removed when accessing the cache.

O(log n) complexity for set and get operations due to heap management.