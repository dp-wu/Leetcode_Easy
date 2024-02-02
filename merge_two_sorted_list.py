# relink two singly linked lists into one singly linked list in ascending order
# this way I don't need to create a new list.
# hence this solution is fast and does not require much memory


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # edge cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # create cursor node
        if list1.val < list2.val:
            pointer = list1
            list1 = list1.next
        else:
            pointer = list2
            list2 = list2.next

        # lock-in the head node
        head = pointer

        # 'sew' the two lists together
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        # append the remaining nodes
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2

        return head
