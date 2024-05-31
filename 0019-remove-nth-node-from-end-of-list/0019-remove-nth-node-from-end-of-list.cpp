/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {         
        if(n == 1 && head->next==NULL) return NULL; 
        ListNode* temp=head;
        int size=0;
        while(temp!=NULL){
            temp=temp->next;
            size++;
           
        }
        
        int tobeRemoved=(size-n);
        temp=head;
        for(int i=1;i<tobeRemoved;i++){
            temp= temp->next;
        }
        cout<<tobeRemoved;
        if(tobeRemoved != 0) { 
        temp->next = temp->next->next;
        }
        else{
            head=head->next;
        }
        return head;
    }
};