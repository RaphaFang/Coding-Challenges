class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    # print(node.value)
    # print(node.left.value)
    # print(node.right.value)

    if not node:
        return []

    result = []
    queue = [node]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left) # 若存在左邊，再把這個node物件加進去queue
        if current_node.right:
            queue.append(current_node.right)

    return result


    # 這題要把 輸入的node，當作一個node物件，
    # 因此，以開此只有一個一長串的node物件，不過這物件包含了這物件的左邊質，以及右邊質
    # 只要不斷的讀取左邊右邊，就可以得到一個list，是原先node物件的所有樹狀結構




print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
# [1, 2, 3, 4, 5, 6]