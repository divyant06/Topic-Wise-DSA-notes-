# Experiment 5: Tower of Hanoi
# Recurrence Relation
# T(n) = 2T(n-1) + 1
# Time Complexity
# O(2ⁿ)
# Space Complexity
# O(n)
# Trace for N = 3 (Must Write)

# Move 1: A → C
# Move 2: A → B
# Move 3: C → B
# Move 4: A → C
# Move 5: B → A
# Move 6: B → C
# Move 7: A → C
# move_count = 0   # To count total moves 

def hanoi(n, source, auxiliary, destination):
    global move_count
    
    # Base Case
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        move_count += 1
        return
    
    # Step 1: Move n-1 disks to auxiliary rod
    hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move nth disk to destination
    print("Move disk", n, "from", source, "to", destination)
    move_count += 1
    
    # Step 3: Move n-1 disks from auxiliary to destination
    hanoi(n-1, auxiliary, source, destination)


# -----------------------------
# Main Program
# -----------------------------
n = int(input("Enter number of disks: "))

if n <= 0:
    print("Invalid input! Number must be positive.")
else:
    move_count = 0
    print("Move Sequence:\n")
    hanoi(n, "A", "B", "C")
    
    print("Total Moves:", move_count)
    print("Formula: 2^n - 1")
    print("Time Complexity: O(2^n)")