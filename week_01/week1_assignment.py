#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

# Question 1

print('''
============================================================================
      
    QUESTION 1:

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example: [2,3,4,2,7] target = 10, output = [1,4]

============================================================================
''')

def twoSum(nums, target):
    complements = []
    for i, n in enumerate(nums):
        compl = target - n
        complements.append(compl)

        if compl in nums:
            return [i, list(nums).index(compl)]
    return []

# Test twoSum

a1 = [2,3,4,2,7]
t1 = 10
out1 = twoSum(a1, t1)

print(f'''
Example: {a1}
Target: 10

Expected output: [1,4]
Output: {out1}

___________
''')

a2 = [8, 5, 2, 7, 3, 1, 9, 4, 6, 10]
t2 = 11
out2 = twoSum(a2, t2)

print(f'''
Example: {a2}
Target: 11

Expected output: [0,4]
Output: {out2}

___________
''')

a3 = [15, 3, 6, 8, 2, 7]
t3 = 13
out3 = twoSum(a3, t3)

print(f'''
Example: {a3}
Target: 13

Expected output: [2,5]
Output: {out3}

___________
''')

a4 = [5, 13, 7, 1, 9, 4, 6]
t4 = 28
out4 = twoSum(a4, t4)

print(f'''
Example: {a4}
Target: 28

Expected output: []
Output: {out4}
''')

print('''
###########################################
      
    Time and space complexity:
      Time: O(n) - the worst case scenario is if the sum is not possible and it will scan the entire array once
      Space: O(n) - it needs an ausiliary array to store the complements that can be as big as the original one in the worst case scenario

###########################################
      

''')

# Question 2

print('''
============================================================================

    QUESTION 2:

    Given some arrays with strings on them, find the most common longest prefix among them.
    Example: ["flower","flow","flight"] output = "fl"
      
============================================================================
''')

def findMostCommonPrefix(arr):
    if len(arr) == 0 or "" in arr:
        return ""
    
    for j, c in enumerate(arr[0]):
        for i in range(1, len(arr)):
            if j >= len(arr[i]) or c != arr[i][j]:
                return arr[0][:j]
    return arr[0]

# Test findMostCommonPrefix

a1 = []
a2 = ["flight", "", "kind"]
a3 = ["flower","flow","flight"]
a4 = ["flyer", "fly"]
a5 = ["app", "apple", "application"]
a6 = ["ape", "apple", "application", "grace", "grave", "zebra"]

print(f'''
Original array: {a1}
      
Expected output: 
Output: {findMostCommonPrefix(a1)}

___________


Original array: {a2}
      
Expected output: 
Output: {findMostCommonPrefix(a2)}

___________


Original array: {a3}
      
Expected output: fl
Output: {findMostCommonPrefix(a3)}

___________


Original array: {a4}
      
Expected output: fly
Output: {findMostCommonPrefix(a4)}

___________


Original array: {a5}
      
Expected output: app
Output: {findMostCommonPrefix(a5)}

___________


Original array: {a6}
      
Expected output: 
Output: {findMostCommonPrefix(a6)}

''')

print('''
###########################################
      
    Time and space complexity:
      Time: O(n * m) - where m is the length of the first string in the array
      Space: O(1) - it does not use more memory other than the input string array itself

###########################################
      

''')

# Question 3

print('''
============================================================================
      
    QUESTION 3:
      
    Given an array of integers, return the indices of three numbers that add up to 0.
    example: [1, 2, -2, -1, 3] output = [2, 3, 4]

============================================================================
''')

def threeSum(nums):
    nums_len = len(nums)

    if nums_len < 3:
        return []

    for i in range(nums_len-2):
        scanned = {}
        target = 0 - nums[i]

        for j in range(i+1, nums_len):
            compl = target - nums[j]

            if compl in scanned:
                return [i, scanned[compl], j]

            scanned[nums[j]] = j

    return []

# Test threeSum

a1 = [1, 2, -2, -1, 3]
a2 = [4, 10, -3, 5, -8, -7]
a3 = [4, 1, -2, -3, 6, -4]
a4 = [2, 3, 1, 2, -4, -1]
a5 = [1, 2, 3, 4, 5]
a6 = []
a7 = [1, 2]

print(f'''
Array: {a1}

Expected output: [2, 3, 4]
Output: {threeSum(a1)}

___________


Array: {a2}

Expected output: [1, 2, 5]
Output: {threeSum(a2)} 

___________


Array: {a3}

Expected output: [2, 4, 5]
Output: {threeSum(a3)}

___________


Array: {a4}

Expected output: [0, 3, 4]
Output: {threeSum(a4)}

___________


Array: {a5}

Expected output: []
Output: {threeSum(a5)}

___________


Array: {a6}

Expected output: []
Output: {threeSum(a6)}

___________


Array: {a7}

Expected output: []
Output: {threeSum(a7)}

''')

print('''
###########################################

    Time and space complexity:
      Time: O(n^2) - the iteration will take at worst n + (n-1) + (n-2) + ... + 1 iterations to complete, which is equivalent to O(n^2)
      Space: O(n) - since we need the original array to get the right indexes, we will need to copy the sorted array elsewhere
      
###########################################
      

''')

# Question 4

print('''
============================================================================
      
    QUESTION 4:
        
    Given a singly linked list, reverse the nodes of the linked list
    Example 1: [1, 2, 3] output = [3, 2, 1]
      
============================================================================
''')

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    out_str = ""
    while head:
        out_str += f"{head.data} "
        head = head.next
    return out_str

def reverseList(head):
    if head is None or head.next is None:
        return head
    
    prev = None
    cur = head
    nxt = head.next

    while not cur is None:
        cur.next = prev
        
        if nxt is None:
            break
        
        prev = cur
        cur = nxt
        nxt = cur.next

    return cur
        
# Test reverseList

head1 = Node(1)
middle1 = Node(2)
tail1 = Node(3)

head1.next = middle1
middle1.next = tail1
tail1.next = None

print(f'''
Original list: {printList(head1)}
Reversed list: {printList(reverseList(head1))}

___________
''')

head2 = None

print(f'''      
Original list: {printList(head2)}
Reversed list: {printList(reverseList(head2))}

___________
''')

head3 = Node(4)
head3.next = None

print(f'''      
Original list: {printList(head3)}
Reversed list: {printList(reverseList(head3))}

___________
''')

head4 = Node(10)
n1 = Node(4)
n2 = Node(23)
n3 = Node(7)
tail4 = Node(15)

head4.next = n1
n1.next = n2
n2.next = n3
n3.next = tail4
tail4.next = None

print(f'''       
Original list: {printList(head4)}
Reversed list: {printList(reverseList(head4))}

''')

print('''
###########################################
      
    Time and space complexity:
      Time: O(n) - it actually is exactly n since it will need to iterate each node
      Space: O(1) - it does not use more memory than what is already allocated for the original list itself, aside from 3 pointers
      
###########################################
      

''')



