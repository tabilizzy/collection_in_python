'''
7. Write a Python program to create a deque and append a few elements to the left and right.
Next, remove some elements from the left and right sides and reverse the deque.
Sample Output:
deque(['Red', 'Green', 'White'])
Adding to the left:
deque(['Pink', 'Red', 'Green', 'White'])
Adding to the right:
deque(['Pink', 'Red', 'Green', 'White', 'Orange'])
Removing from the right:
deque(['Pink', 'Red', 'Green', 'White'])
Removing from the left:
deque(['Red', 'Green', 'White'])
Reversing the deque:
deque(['White', 'Green', 'Red'])
'''
import collections
from collections import deque

deque = deque(['Red', 'Green', 'White'])

#add element to the left
deque.appendleft('pink')
#add elements to the right
deque.append('orange')
print(deque)

#remove from the right
deque.pop()
#remove from the left
deque.popleft()
print(deque)

#reversing the deque
deque.reverse()
print(deque)

'''
8. Write a Python program to create a deque from an existing 
iterable object.
Sample Output:
Original tuple:
(2, 4, 6)
<class 'tuple'>
Original deque:
deque([2, 4, 6])
New deque from an existing iterable object:
deque([2, 2, 4, 6, 8, 10, 12])
<class 'collections.deque'>
'''
# creating the tuple
this_tuple = (2,4,6)
print(f"Original tuple: {this_tuple}")
print(type(this_tuple))

#converting the tuple to a deque
original_deque = collections.deque(this_tuple)
print(f"Original deque: {original_deque}")

#adding elements to the left and the right
original_deque.appendleft(2)
original_deque.append(8)
original_deque.append(10)
original_deque.append(12)
print(original_deque)
print(type(original_deque))



