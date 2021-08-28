class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_List:

    def __init__(self):
        self.head = None

    # printing the value in Linked List
    def print(self):

        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + " --> "
            itr = itr.next
        print(lstr)

    # getting the length of the Linked List
    def get_length(self):

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # Inserting the data value at the beginning of the Linked List
    def insert_at_beginning(self, data):

        node = Node(data, self.head)
        self.head = node

    # Inserting the data value at the end of the Linked List
    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # insert at the data value at given index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("Invalid Index")

        if index == 0:
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # insert data after the specific value
    def insert_after_value(self, insert_after, data_to_insert):

        if self.head is None:
            return -1

        if self.head.data == insert_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == insert_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    # insert the full list to the linked list
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # remove at the specific index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # Remove by the specific data value
    def remove_by_value(self, data):
        if self.head is None:
            return -1

        if self.head.data == data:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = Linked_List()
    ll.insert_at_beginning("banana")
    ll.insert_at_beginning("orange")
    ll.insert_at_end("jackfruit")
    ll.print()
    print("The length of the list ", ll.get_length())
    ll.insert_value(['pencil', 'bag', 'eraser', 'pen'])
    ll.print()
    ll.insert_at_end('compassbox')
    # ll.print()
    # ll.remove_at(0)
    # ll.print()
    # ll.remove_by_value('bag')
    # ll.print()
    # ll.remove_at(1)
    # ll.print()
    ll.print()
    ll.insert_after_value('pen','laptop')
    ll.print()
