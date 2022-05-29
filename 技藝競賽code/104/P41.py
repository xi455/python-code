class tree:
    def __init__(self ,node):
        self.node = node
        self.left = None
        self.right = None
   
    def insert(self ,value):
        if self.node:
            if value < self.node:
                if self.left is None:
                    self.left = tree(value)
                else:
                    self.left.insert(value)
            elif value > self.node:
                if self.right is None:
                    self.right = tree(value)
                else:
                    self.right.insert(value)
            else:
                self.node = value
 
    def prvalue(self ,value = []):
        if self.left:
            self.left.prvalue()
 
        if self.right:
            self.right.prvalue()
       
        value.append(str(self.node))
        return value
cont = 0
for T in range(int(input())):
    node_num = int(input())
    node = list(map(int,input().strip().split(',')))
    root = tree(node[0])
    for i in range(1,node_num):
        root.insert(node[i])
    cont += node_num
    print(','.join(root.prvalue()[cont - node_num:]))
