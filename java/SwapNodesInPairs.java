/*

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

*/


package summer;

/**
 *
 * @author Ziheng
 */
class ListNode{
    int val;
    ListNode next;
    ListNode(int x){val = x;}
}

public class Summer {
    
    // 这道题属于链表操作的题目，思路比较清晰，就是每次跳两个节点，后一个接到前面，
    // 前一个接到后一个的后面，最后现在的后一个（也就是原来的前一个）接到下下个结点（如果没有则接到下一个）。
    // 这道题中用了一个辅助指针作为表头，这是链表中比较常用的小技巧，
    // 因为这样可以避免处理head的边界情况，一般来说要求的结果表头会有变化的会经常用这个技巧。
    public ListNode swapPairs(ListNode head){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curnt = dummy;
        while (curnt.next != null && curnt.next.next != null){
            ListNode first = curnt.next;
            ListNode second = curnt.next.next;
            first.next = second.next;
            curnt.next = second;
            curnt.next.next = first;
            curnt = curnt.next.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode A = new ListNode(1);
        ListNode B = new ListNode(2);
        ListNode C = new ListNode(3);
        ListNode D = new ListNode(4);
        ListNode E = new ListNode(5);
        A.next = B; B.next = C; C.next = D; D.next = E;
        Summer Start = new Summer();
        System.out.println(Start.swapPairs(A).val);
        System.out.println(Start.swapPairs(B).val);
        System.out.println(Start.swapPairs(C).val);
        System.out.println(Start.swapPairs(D).val);
        System.out.println(Start.swapPairs(E).val);
        
    }
    
}
