class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
     if(root==None):
        newnode = BinaryTreeNode(key)
        root = newnode
        
     elif(new_value<root.data):
         root.left = insert(root.left,new_value)
        
     else:
         root.right = insert(root.right,new_value)
     
     return root
    
def inorder(root) -> None:
    if (root and root.left):
        inorder(root.left)
    
    elif(root.left==None):
        print(root.data)
    
    elif(root.right==None):
        


def preorder(root) -> None:
    # Write your code here


def postorder(root) -> None:
    # Write your code here


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
