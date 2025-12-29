# Implementation of LinkedList was copied from the syllabus "as is"

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


    # TASK 1: Reverse List
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to current
            current = next_node  # Move current to next
        self.head = prev  # Update head to the last processed node

    # TASK 2: Insertion Sort
    def insertion_sort(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next  # Store next to iterate later

            # Insert current into the sorted list
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                # Find the insertion point in the sorted part
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node  # Move to the next node in the original list

        self.head = sorted_head


# TASK 3: Merge Two Sorted Lists
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()

    # Create a dummy node to simplify the logic
    dummy = Node()
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append the remaining nodes if any
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    # The head of the new list is the next of dummy
    merged_list.head = dummy.next
    return merged_list


# --- Testing of the new methods ---
def main() -> None:
    print("--- 1. Reversing ---")
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    print("Original:")
    ll.print_list()
    ll.reverse()
    print("Reversed:")
    ll.print_list()

    print("\n--- 2. Insertion Sort ---")
    ll_sort = LinkedList()
    ll_sort.insert_at_end(4)
    ll_sort.insert_at_end(2)
    ll_sort.insert_at_end(1)
    ll_sort.insert_at_end(3)
    print("Unsorted:")
    ll_sort.print_list()
    ll_sort.insertion_sort()
    print("Sorted:")
    ll_sort.print_list()

    print("\n--- 3. Merge Sorted Lists ---")
    list_a = LinkedList()
    list_a.insert_at_end(1)
    list_a.insert_at_end(3)
    list_a.insert_at_end(5)

    list_b = LinkedList()
    list_b.insert_at_end(2)
    list_b.insert_at_end(4)
    list_b.insert_at_end(6)

    print("List A:")
    list_a.print_list()
    print("List B:")
    list_b.print_list()

    merged = merge_sorted_lists(list_a, list_b)
    print("Merged List:")
    merged.print_list()


if __name__ == "__main__":
    main()
