# 1. Dynamic Array (No imports version)
class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = [None] * self.capacity

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0: return None
        val = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return val

    def _resize(self, new_cap):
        B = [None] * new_cap
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

# 2. Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

# 3. Stack & Queue using SLL
class Stack:
    def __init__(self):
        self.top = None
    def push(self, d):
        new = Node(d); new.next = self.top; self.top = new
    def pop(self):
        if not self.top: return None
        res = self.top.data; self.top = self.top.next; return res

class Queue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, d):
        new = Node(d)
        if not self.rear: self.front = self.rear = new; return
        self.rear.next = new; self.rear = new
    def dequeue(self):
        if not self.front: return None
        res = self.front.data; self.front = self.front.next
        if not self.front: self.rear = None
        return res

# 4. Bracket Checker
def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in "([{": s.push(char)
        elif char in ")]}":
            if not s.top or s.pop() != pairs[char]: return False
    return s.top is None
# Execution 
if __name__ == "__main__":
    da = DynamicArray(); da.append(5); print("Array Pop:", da.pop())
    st = Stack(); st.push(10); print("Stack Pop:", st.pop())
    print("Balanced '{[()]}':", is_balanced("{[()]}"))
