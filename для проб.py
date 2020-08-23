class Point:
    name='Class=Point'
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def show(self):
        print('pt.x={}\tpt.y={}'.format(self.x,self.y))
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
Point.name='Hello word'
pt1 = Point(4,7)
print(id(pt1), pt1.x, pt1.y,pt1.name)
pt1.x=6
print(id(pt1), pt1.x, pt1.y)
pt2 = Point()
print(id(pt2), pt2.x, pt2.y,pt2.name)
pt3 = Point()
print(id(pt3), pt3.x, pt3.y,pt3.name)
pt1.show()
pt1.move(5,6)
pt1.show()


