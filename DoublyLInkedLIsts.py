# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # insert after a given value
    def insert_after(self, target, value):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(value)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    # delete at position
    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # delete head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            temp = temp.next
            if temp is None:
                print("Position not valid")
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# main
dll = DoublyLinkedList()

# manually creating list
dll.head = Node(10)
n2 = Node(20)
n3 = Node(30)

dll.head.next = n2
n2.prev = dll.head
n2.next = n3
n3.prev = n2

print("List:")
dll.display()

dll.insert_after(20, 25)
print("After insertion:")
dll.display()

dll.delete_pos(2)
print("After deletion:")
dll.display()