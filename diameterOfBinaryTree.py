
# 返回二叉树中的任意两个节点之间最长路径的长度，原题543
def diameterOfBinaryTree(root) -> int:
    """
    1. 在当前节点转折，路径长=（左子节点路径长+1）加上（右子节点路径长+1）
    2. return什么？将左右子节点更长的路径归给父节点
    3. 边界条件？叶子节点的话路径为0，因此遇到空时返回-1
    """
    ans = 0
    def dfs(node):
        if node is None:
            return -1
        left = dfs(node.left) + 1
        right = dfs(node.right) + 1
        nonlocal ans
        ans = max(ans, left + right)
        return max(left, right)
    dfs(root)
    return ans

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

case_1 = [1,2,3,4,5]
case_2 = [1,2]


def build_tree(l):
    nodes = []
    for x in l:
        if x is not None:
            nodes.append(TreeNode(x))
        else:
            nodes.append(None)
    for i in range(len(nodes)):
        if nodes[i]:
            if 2*i+1 < len(nodes):
                nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(nodes):
                nodes[i].right = nodes[2*i+2]
    if nodes:
        return nodes[0]
    return None

tree_1 = build_tree(case_1)
tree_2 = build_tree(case_2)
print(diameterOfBinaryTree(tree_1))
print(diameterOfBinaryTree(tree_2))
