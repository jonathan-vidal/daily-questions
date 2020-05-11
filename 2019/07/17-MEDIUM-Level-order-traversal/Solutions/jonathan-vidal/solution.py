def level_order_traversal(tree):
    levels = [[tree[0]]]    # root of the tree

    for depth in range(len(tree)):
        if 2*depth+1 >= len(tree):
            break

        leaves = []
        if tree[2*depth+1] is not None:
            leaves.append(tree[2*depth+1])

        if tree[2*depth+2] is not None:
            leaves.append(tree[2*depth+2])

        if leaves:
            levels.append(leaves)

    return levels