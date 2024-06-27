# Excercise 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
         return "This calculates the distance between the two points."
    
    def distance(x, y):
        return (x - y)

print(Point.distance(2,1))

#Excercise 2

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
         return "This calculates the length of a line."
    
    def length(point1 , point2):
        return float(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5)
    
    def slope(point1, point2):
        slope1 = float((point2[1] - point1[1])/(point2[0] - point1[0]))
        return slope1
    
    def point_on_line(point, point3):
        self.point3 = point3
        return point3[1] == li


# Excercise 3

import matplotlib.pyplot as plt
class shape(Line):

    def __init__(self,List):
        self.List=List

    def __str__(self):
        return "Please enter the points to draw the shape"
    
    
    def draw_lines(List):
       for Line in List:
           Line = ((x1, y1), (x2, y2))
           plt.plot([x1, x2], [y1, y2],)
    

    #plt.show()

list: [((0, 0), (1, 0)),((1, 0), (0.5, 1)),((0.5, 1), (0, 0))]
    
shape.draw_lines(list)




