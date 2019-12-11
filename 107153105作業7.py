class node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None
  def setLeft(self, left):
    self.left = left
  def setRight(self, right):
    self.right = right
p1 = node('A')
root = p1
p2 = node('B')
p3 = node('C')
p4 = node('D')
p5 = node('E')
p7 = node('F')
p1.setLeft(p2)
p1.setRight(p3)
p2.setLeft(p4)
p2.setRight(p5)
p3.setRight(p7)
qu = []
def levelorder(now):
    qu.append(now)
    while (len(qu)>0):
        print(qu[0].val, sep=' ', end = '')
        if qu[0].left != None:
            qu.append(qu[0].left)
        if qu[0].right != None:
            qu.append(qu[0].right)
        del qu[0]
levelorder(root)
print()
