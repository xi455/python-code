def root(inorder):
    for i in range(len(preorder)):
        if preorder[i] in inorder:
            num_list.insert(0,preorder[i])
            tree_left = inorder[:inorder.index(preorder[i])]
            tree_right = inorder[inorder.index(preorder[i]) + 1:]
            break
 
    if tree_right != []:
        root(tree_right)
 
    if tree_left != []:
        root(tree_left)
 
for T in range(int(input())):
    inorder = input().strip().split(',')
    preorder = input().strip().split(',')
    num_list = []
 
    root(inorder)
    print(','.join(num_list))
