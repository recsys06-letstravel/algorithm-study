class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next

class LinkedList:
    # Function to initialize head
    def __init__(self, k):
        self.head = None
        self.position = k
        self.deleted = []
        self.length = 0

    def now_value(self):
        temp = self.head
        for _ in range(self.position):
            temp = temp.next
        return temp.data

    def append(self, new_data):
        new_node = Node(new_data)
        self.length += 1
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        # 6. Change the next of last node
        last.next = new_node

    def insertVal(self):
        val = self.deleted.pop()
        now_val = self.now_value()
        if val < now_val:
            self.position += 1
        new_node = Node(val)
        self.length += 1
        temp = self.head
        if temp.next is None:
            temp.next = new_node
        while temp.next:
            if temp.next.data > val:
                break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    # def deleteNode(self, key):
    #     # Store head node
    #     temp = self.head
    #     # If head node itself holds the key to be deleted
    #     if (temp is not None):
    #         if (temp.data == key):
    #             self.head = temp.next
    #             temp = None
    #             return
    #     # Search for the key to be deleted, keep track of the
    #     # previous node as we need to change 'prev.next'
    #     while (temp is not None):
    #         if temp.data == key:
    #             break
    #         prev = temp
    #         temp = temp.next
    #     # if key was not present in linked list
    #     if (temp == None):
    #         return
    #     # Unlink the node from linked list
    #     prev.next = temp.next
    #     temp = None

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        result = []
        while (temp):
            result.append(temp.data)
            temp = temp.next
        print(result)

    def delete(self):
        temp = self.head
        self.length -= 1
        val = 0
        for _ in range(self.position):
            prev = temp
            temp = temp.next

        if temp is not None:
            prev.next = temp.next
            val = temp.data
            temp = None
        self.deleted.append(val)
        if self.length <= self.position:
            self.position -= 1
        # return val

    def change_position(self, num):
        self.position += num

    def ans(self):
        temp = self.head
        index = 0
        result = ""
        while temp:
            if index == temp.data:
                result += 'O'

            else:
                while index != temp.data:
                    result += 'X'
                    index += 1
                result += 'O'
            # result.append(temp.data)
            temp = temp.next
            index += 1
        return result


def solution(n, k, cmd):
    # result = LinkedList(k)
    # for i in range(n):
    #     result.append(i)
    #
    # now_position = k
    # for i in cmd:
    #     command = i.split()
    #     if len(command) == 2:
    #         if command[0] == 'D':
    #             result.change_position(int(command[1]))
    #             # now_position = now_position + int(command[1])
    #         elif command[0] == 'U':
    #             result.change_position(-int(command[1]))
    #             now_position = now_position - int(command[1])
    #     elif len(command) == 1:
    #         if command[0] == 'C':
    #             result.delete()
    #         elif command[0] == 'Z':
    #             result.insertVal()
    # answer = result.ans()

    # # print(answer)
    # for i in range(n):
    #     if i in temp:
    #         answer += 'O'
    #     else:
    #         answer += 'X'
    position = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    stack = []
    answer = ["O"] * n
    for i in cmd:
        command = i.split()
        if len(command) == 2:
            if command[0] == 'D':
                for _ in range(int(command[1])):
                    position = table[position][1]
            elif command[0] == 'U':
                for _ in range(int(command[1])):
                    position = table[position][0]
        elif len(command) == 1:
            if command[0] == 'C':
                answer[position] = "X"
                prev, next = table[position][0], table[position][1]
                stack.append([prev, position, next])
                # 포지션 정리
                if next is None:
                    position = table[position][0]
                else:
                    position = table[position][1]
                # 연결성 정리
                if prev is None:
                    table[next][0] = None
                elif next is None:
                    table[prev][1] = None
                else:
                    table[prev][1], table[next][0] = next, prev

            elif command[0] == 'Z':
                prev, cur, next = stack.pop()
                answer[cur] = "O"
                if prev is None:
                    table[next][0] = cur
                elif next is None:
                    table[prev][1] = cur
                else:
                    table[prev][1], table[next][0] = cur, cur

    return ''.join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))