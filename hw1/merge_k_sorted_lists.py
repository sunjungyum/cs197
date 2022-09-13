import heapq as h

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    # initiliaize min heap using heapify
    min_heap = []
    h.heapify(min_heap)

    # initialize 'start' node of output linked list
    output_start = ListNode(val=-1)
    cur = output_start

    # iterate through lists, pushing k heads onto the min heap
    for i, head in enumerate(lists):
        if head:
            h.heappush(min_heap, (head.val, i))

    # while min heap has elements
    while min_heap:
    #   pop the minimum and add it to the output linked list
        _, temp_i = h.heappop(min_heap)
        cur.next = lists[temp_i]

    #   iterate the runner
        cur = cur.next

    #   push the popped element's 'next' onto the min heap (if not None)
        if lists[temp_i].next:
            lists[temp_i] = lists[temp_i].next
            h.heappush(min_heap, (lists[temp_i].val, temp_i))

    # return the 'next of the 'start' node
    return output_start.next

def make_linked_lists(klists):
    lists = [0] * len(klists)

    for i, klist in enumerate(klists):
        start = ListNode(val=-1)
        cur = start
        for value in klist:
            cur.next = ListNode(val=value)
            cur = cur.next
        lists[i] = start.next
    return lists

def print_linked_list(head):
    output_string = ""

    cur = head
    while cur:
        output_string += str(cur.val)
        if cur.next:
            output_string += " -> "
        cur = cur.next
    print(output_string)

def test():
    test_klists = make_linked_lists([[1,4,5],[1,3,4],[2,6]])
    for linked_list in test_klists:
        print_linked_list(linked_list)
    test_merged_head = mergeKLists(test_klists)
    print_linked_list(test_merged_head)

if __name__ == "__main__":
    test()