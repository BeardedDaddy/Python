graph = {
    1:[2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}

from collections import deque
deque(['a', 'b', 'c'])

deque('abc')

deque([{'data': 'a'}, {'data': 'b'}])

# Linked list to be iterated.
#llist = deque("abcde")
#llist

# Add "f" to the end of the list.
#llist.append("f")
#llist

# Remove the element at the end of the list.
#llist.pop()

# Add the letter "z" at the beginning of the list.
#llist.appendleft("z")
#llist

# Remove the element at the beginning of the list.
#llist.popleft()
#llist

queue = deque()

queue.append("Mary")
queue.append("John")
queue.append("Susan")

queue.popleft()
queue.popleft()

history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")

history.popleft()
history.popleft()
print(history)
