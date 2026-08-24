from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            cursize = len(queue)
            temp = []
            for i in range(cursize):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            res.append(temp)
        return res


