# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #l1.reverse()
        #l2.reverse()
        # s1 = 0
        # s2 = 0
        # ans = []
        # for i in range(len(l1)):
        #     s1 += l1[i] * (10 ** i)
        #     print s1
        # for j in range(len(l2)):
        #     s2 += l2[j] * (10 ** j)
        #     print s2
        #     sum1 = str(s1+s2)
        # for k in sum1:
        #     ans.append(int(k))
        # ans.reverse()
        # return ans
        l3=p=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            p.next = ListNode(carry % 10)
            p=p.next
            carry=carry//10
        return l3.next

if __name__ == '__main__':
    S = Solution()
    print S.addTwoNumbers([2, 4, 3], [5, 6, 4])

