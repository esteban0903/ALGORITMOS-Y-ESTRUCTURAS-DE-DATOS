def postOrderFromPreIn(preorder, inorder):
    if not preorder:
        return []

    root = preorder[0]
    root_idx = inorder.index(root)

    left_pre = preorder[1:root_idx + 1]
    #print("left_pre",left_pre)
    right_pre = preorder[root_idx + 1:]
    #print("right_pre", right_pre)

    left_in = inorder[:root_idx]
    #print("left_in", left_in)
    right_in = inorder[root_idx + 1:]
    #print("right_in", right_in)

    left_post = postOrderFromPreIn(left_pre, left_in)
    right_post = postOrderFromPreIn(right_pre, right_in)

    pos = left_post + right_post + [root]
    return pos


def main():
    pre = [1, 2, 4, 5, 3, 6, 7]
    ino = [4, 2, 5, 1, 6, 3,7]
    pos = postOrderFromPreIn(pre, ino)
    print("Pre",pre)
    print("Ino", ino)
    print("Pos",pos)


main()