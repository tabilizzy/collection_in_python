'''
9. Write a Python program to add more elements to a deque object
from an iterable object.
Sample Output:
Even numbers:
deque([2, 4, 6, 8, 10])
More even numbers:
deque([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
'''

import collections
from collections import deque

even = deque([2, 4, 6, 8, 10])
print(even)
even.extend([12, 14, 16, 18, 20])
print(even)

'''
10. Write a Python program to remove all the elements of a given deque object. Scripting Languages
Sample Output:
Original Deque object with odd numbers:
deque([1, 3, 5, 7, 9])
Deque length: 5
Deque object after removing all numbers- deque([])
Deque length:0
'''
odd_deque = deque([1, 3, 5, 7, 9])
print(len(odd_deque))

odd_deque.clear()
print(len(odd_deque))
