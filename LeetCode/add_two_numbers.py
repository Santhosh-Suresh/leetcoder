# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        n1 = l1
        stack1 = []
        while n1 is not None:
            stack1.append(n1.val)
            n1 = n1.next

        n2 = l2
        stack2 = []
        while n2 is not None:
            stack2.append(n2.val)
            n2 = n2.next

        carry = 0
        ans_stack = []

        # print(stack1)
        # print(stack2)

        while stack1 or stack2:

            s1 = stack1.pop() if stack1 else 0
            s2 = stack2.pop() if stack2 else 0

            val = (s1 + s2 + carry) % 10
            carry = (s1 + s2 + carry) // 10
            #   print(val, carry)
            ans_stack.append(val)
        else:
            if carry:
                ans_stack.append(carry)

        # print(ans_stack)

        ans = ListNode()
        curr = ans

        while len(ans_stack) > 1:
            curr.val = ans_stack.pop()
            curr.next = ListNode()
            curr = curr.next
        else:
            if ans_stack:
                curr.val = ans_stack.pop()
                curr.next = None
                return ans
            else:
                return None