#Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insertAt(self, index, data):
        if index < 0 or index >= self.size():
            return
        node = Node(data)
        current = self.head
        previous = None
        count = 0
        if index == 0:
            self.head = Node(data, node)
        else:
            while count != index:
                count += 1
                previous = current
                current = current.next
            new_node = Node(data, previous.next)
            previous.next = new_node

    def removeAt(self, index):
        if index < 0 or index >= self.size():
            return
        current = self.head
        previous = None
        count = 0
        if index == 0:
            self.head = current.next
        else:
            while count != index:
                count += 1
                previous = current
                current = current.next
            previous.next = current.next

    def remove(self, data, all=False):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                    current.next = current
                else:
                    self.head = current.next
                if not all:
                    return
            else:
                previous = current
                current = current.next

    def indexOf(self, data):
        node = self.head
        count = 0
        while node:
            if node.data == data:
                return count
            count += 1
            node = node.next

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def print(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> "
            print(node.data, end=end)
            node = node.next


ll = LinkedList()
print(ll.isEmpty())#True
ll.append(10)
ll.append(20)
print(ll.isEmpty())#False
print(ll.print())#10 -> 20 -> None
ll.insertAt(1,60)
print(ll.print())#10 -> 60 -> 20 -> None
ll.append(20)
print(ll.print())#10 -> 60 -> 20 -> 20 -> None
ll.remove(20)
print(ll.print())#10 -> 60 -> 20 -> None
ll.removeAt(1)
print(ll.print())#10 -> 20 -> None
ll.remove(20)
print(ll.size())#1
print(ll.print())#10 -> None