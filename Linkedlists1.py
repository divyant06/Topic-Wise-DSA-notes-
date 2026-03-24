# ---------------- LINKED LIST PROGRAM IN PYTHON ----------------
# Linked List is a linear data structure
# It is made of nodes
# Each node has two parts:
# 1. data  -> stores the value
# 2. next  -> stores address of next node


# ---------------- NODE CLASS ----------------
# class keyword is used to create a class
class Node:
    
    # __init__ is a constructor
    # It is automatically called when object is created
    def __init__(self, data):
        # self refers to the current object
        # data stores the value of the node
        self.data = data
        
        # next stores address of next node
        # Initially it is set to None
        self.next = None


# ---------------- LINKED LIST CLASS ----------------
class LinkedList:
    
    # Constructor of LinkedList
    def __init__(self):
        # head stores address of first node
        # Initially list is empty, so head is None
        self.head = None


    # ---------------- INSERT OPERATION ----------------
    # This function inserts node at the end
    def insert(self):
        # input() takes value from user
        # int() converts input to integer
        value = int(input("Enter value to insert: "))
        
        # Create new node using Node class
        new_node = Node(value)
        
        # If linked list is empty
        if self.head is None:
            # New node becomes first node
            self.head = new_node
            print("Node inserted as first node")
        else:
            # temp is used to traverse the list
            temp = self.head
            
            # Traverse till last node
            while temp.next is not None:
                temp = temp.next
            
            # Link last node to new node
            temp.next = new_node
            print("Node inserted at end")


    # ---------------- DELETE OPERATION ----------------
    # This function deletes first node
    def delete(self):
        # If list is empty
        if self.head is None:
            print("Linked list is empty, cannot delete")
        else:
            # Store head node in temp
            temp = self.head
            
            # Move head to next node
            self.head = self.head.next
            
            # Delete reference of temp
            del temp
            print("First node deleted")


    # ---------------- TRAVERSAL OPERATION ----------------
    # This function displays all nodes
    def traversal(self):
        # If list is empty
        if self.head is None:
            print("Linked list is empty")
        else:
            print("Linked list elements are:")
            
            # temp starts from head
            temp = self.head
            
            # Loop till last node
            while temp is not None:
                # Print data of each node
                print(temp.data)
                
                # Move to next node
                temp = temp.next


    # ---------------- SEARCH OPERATION ----------------
    # This function searches a value in list
    def search(self):
        # input() takes value to search
        value = int(input("Enter value to search: "))
        
        # temp starts from head
        temp = self.head
        
        # position keeps track of node number
        position = 1
        
        # Traverse list
        while temp is not None:
            # If value found
            if temp.data == value:
                print("Value found at position", position)
                return
            
            # Move to next node
            temp = temp.next
            position += 1
        
        # If value not found
        print("Value not found in linked list")


# ---------------- MAIN PROGRAM ----------------
# Create LinkedList object
ll = LinkedList()

# Infinite loop for menu driven program
while True:
    print("\nLinked List Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Search")
    print("5. Exit")
    
    # Take user choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        ll.insert()
    elif choice == 2:
        ll.delete()
    elif choice == 3:
        ll.traversal()
    elif choice == 4:
        ll.search()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice, try again")