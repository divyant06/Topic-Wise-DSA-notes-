# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # delete by value
    def delete(self, value):
        temp = self.head

        # if head is to be deleted
        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    # display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# main
ll = LinkedList()

ll.insert_begin(10)
ll.insert_begin(5)
ll.insert_end(20)
ll.insert_end(30)

print("List:")
ll.display()

ll.delete(20)

print("After deletion:")
ll.display()