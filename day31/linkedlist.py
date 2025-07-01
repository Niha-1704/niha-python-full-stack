# Head Node[1,next] => [2,next] => [3,next] => tail Node [4, None]

class Node:
    def __init__(self , value = 0 , nextNode = None):
        self.val = value
        self.next = nextNode    

# item1 = Node(100)
# item2 = Node(200)
# item3 = Node(300)
# item4 = Node(400)
# item5 = Node(500)

# item1.next = item2
# item2.next = item3
# item3.next = item4
# item4.next = item5
# print(item3.next.next.val)



# head = Node(100)
# head.next = Node(200)
# head.next.next = Node(300)
# head.next.next.next = Node(400)
# head.next.next.next.next = Node(500)

# print(head)
# print(head.next.val)
# print(head.next.next.next.next.val)
# print(head.next.next.next.next.next)

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500)

def display(head):
    current = head
    res = []
    c = 0
    while current != None:
        c += 1
        res.append(str(current.val))
        current = current.next
    print(" => ".join(res))
    print(c)



#adding element at last in linkedlist

# current = head
# while current.next != None:
#     current = current.next
# current.next = Node(int(input()))
# display(head)



#adding element at the start

# new = Node(int(input()))
# new.next = head
# head = new
# display(head)


#adding element at particular position


# position = 1
# value = 250
# newNode = Node(value)
# current = head
# node_position = 0
# if position == 1:
#     newNode.next = head
#     head = newNode

# while current != None:
#     node_position += 1
#     if node_position == position - 1:
#         temp = current.next
#         current.next = newNode
#         newNode.next = temp
#     current = current.next

# display(head)


# deleting particular element

value = int(input())
current = head
while current != None:
    if current.val == value:
        current.val = current.next.val
        current.next = current.next.next
    current.next = next