'''
Solving Leetcode Problem.
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
import heapq as h


class ListNode(object):
    '''
    ListNode class type for linked-list implementation.

    'val' attribute gives integer value, and 'next' attribute gives
    the next ListNode
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    '''
    Calls the appropriate merging function (iterative or recursive).
    '''
    return merge_k_lists_iter(lists)
    # Extra Credit:
    # return merge_k_lists_recurs(lists)


def merge_k_lists_iter(lists):
    '''
    Returns a sorted linked-list given a list of sorted linked-lists
    using an interative algorithm.
    :type lists: List[ListNode]
    :rtype: ListNode
    '''
    min_heap = []
    h.heapify(min_heap)

    output_start = ListNode(val=-1)
    cur = output_start

    for i, head in enumerate(lists):
        if head:
            h.heappush(min_heap, (head.val, i))

    while min_heap:
        _, temp_i = h.heappop(min_heap)
        cur.next = lists[temp_i]
        cur = cur.next

        if lists[temp_i].next:
            lists[temp_i] = lists[temp_i].next
            h.heappush(min_heap, (lists[temp_i].val, temp_i))

    return output_start.next


def merge_k_lists_recurs(lists):
    '''
    EXTRA-CREDIT
    Returns a sorted linked-list given a list of sorted linked-lists
    using a recursive algorithm.
    :type lists: List[ListNode]
    :rtype: ListNode
    '''
    k = len(lists)
    dist = 1

    if k <= 0:
        return None

    while dist < k:
        for i in range(0, k - dist, dist * 2):
            lists[i] = merge_adj_lists(lists[i], lists[i + dist])
        dist *= 2

    return lists[0]


def merge_adj_lists(list1, list2):
    '''
    EXTRA-CREDIT
    Merges two sorted linked-lists together, comparing element by element.
    '''
    output_start = ListNode(val=-1)
    cur = output_start

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1

    if list2:
        cur.next = list2

    return output_start.next


'''
Testing functions
'''


def make_linked_lists(klists):
    '''
    Returns a list of linked-lists given a list of lists.
    '''
    lists = [0] * len(klists)

    for i, klist in enumerate(klists):
        start = ListNode(val=-1)
        cur = start
        for value in klist:
            cur.next = ListNode(val=value)
            cur = cur.next
        lists[i] = start.next
    return lists


def output_linked_list(head):
    '''
    Returns a formatted string of linked-list elements given the head
    of linked-list.
    '''
    output_string = ""

    cur = head
    while cur:
        output_string += str(cur.val)
        if cur.next:
            output_string += " -> "
        cur = cur.next
    return output_string


def test_1():
    '''
    Runs test 1, which uses k = 3 with all positive integers.
    '''
    print("Test 1:")
    test_klists = make_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    print("Input: ", end="")
    test_input_string = ""
    for linked_list in test_klists:
        test_input_string += "[" + output_linked_list(linked_list) + "] "
    print(test_input_string)

    test_merged_head = merge_k_lists(test_klists)
    print("Output: [", end="")
    test_output_string = output_linked_list(test_merged_head)
    print(test_output_string + "]")

    answer_string = "1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6"
    print("SUCCESS\n" if test_output_string == answer_string else "FAILURE\n")


def test_2():
    '''
    Runs test 2, which uses k = 5 with negative and positive integers,
    as well as 0.
    '''
    print("Test 2:")
    test_klists = make_linked_lists([
                                        [-1, 4, 5, 9, 11, 12, 30],
                                        [0, 2, 3],
                                        [-2, 5, 6],
                                        [1, 3],
                                        [4, 8, 11, 15, 18]
                                    ])
    print("Input: ", end="")
    test_input_string = ""
    for linked_list in test_klists:
        test_input_string += "[" + output_linked_list(linked_list) + "] "
    print(test_input_string)

    test_merged_head = merge_k_lists(test_klists)
    print("Output: [", end="")
    test_output_string = output_linked_list(test_merged_head)
    print(test_output_string + "]")

    answer_string = '-2 -> -1 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> '\
                    '5 -> 6 -> 8 -> 9 -> 11 -> 11 -> 12 -> 15 -> 18 -> 30'
    print("SUCCESS\n" if test_output_string == answer_string else "FAILURE\n")


def test_3():
    '''
    Runs test 3, an edge case which uses k = 4 with empty lists.
    '''
    print("Test 3:")
    test_klists = make_linked_lists([[], [], [], []])
    print("Input: ", end="")
    test_input_string = ""
    for linked_list in test_klists:
        test_input_string += "[" + output_linked_list(linked_list) + "] "
    print(test_input_string)

    test_merged_head = merge_k_lists(test_klists)
    print("Output: [", end="")
    test_output_string = output_linked_list(test_merged_head)
    print(test_output_string + "]")

    answer_string = ""
    print("SUCCESS\n" if test_output_string == answer_string else "FAILURE\n")


def test_4():
    '''
    Runs test 4, an edge case which uses k = 0.
    '''
    print("Test 4:")
    test_klists = make_linked_lists([])
    print("Input: ", end="")
    test_input_string = ""
    for linked_list in test_klists:
        test_input_string += "[" + output_linked_list(linked_list) + "] "
    print(test_input_string)

    test_merged_head = merge_k_lists(test_klists)
    print("Output: [", end="")
    test_output_string = output_linked_list(test_merged_head)
    print(test_output_string + "]")

    answer_string = ""
    print("SUCCESS\n" if test_output_string == answer_string else "FAILURE\n")


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
