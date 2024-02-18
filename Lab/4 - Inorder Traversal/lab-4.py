# While writing the code always include the below class
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(values):
    root_node = TreeNode(values[0])
    nodes = [root_node]
    for i , x in enumerate(values[1:]):
        if x is None:
            continue
        parent_node = nodes[i//2]
        is_left = i %2 ==0
        node = TreeNode(x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)
    return root_node


#modified level order traversal
def rightView(root:TreeNode)-> list[int]:
    if not root:  # no root then return none
        return None
    right_nodes = []
    queue = deque([root]) # initialize a queue with the root node
    while queue: # as long as there are nodes in the queue
      level_len = len(queue) # get the number of nodes at that level
      for i in range(level_len): # iterate throuh all the nodes at this level
        node = queue.popleft() # pop the left most queeue
        if i == level_len - 1:
                  right_nodes.append(node.val) # if its the last node at the current level add its value to the list
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) # add the child nodes if it existss

    return right_nodes

node = createTree([9, 8, 7, None, None, 7, 8])

