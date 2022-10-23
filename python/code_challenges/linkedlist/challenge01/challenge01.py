class Solution:
    def delete_node(self,node_to_be_deleted):
        '''
        input -> object

        return -> None
        '''
         # 1 -> 5 -> 7 -> 9 -> None
         # node_to_be_deleted=5
        node_to_be_deleted.value= node_to_be_deleted.next.value
        node_to_be_deleted.next= node_to_be_deleted.next.next
        # 1 -> 7 -> 9 -> None 