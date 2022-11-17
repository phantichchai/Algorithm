class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_of_a = (ax2 - ax1) * (ay2 - ay1)
        area_of_b = (bx2 - bx1) * (by2 - by1)
        
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left
        
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom
        
        area_of_overlap = 0
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = x_overlap * y_overlap
        return area_of_a + area_of_b - area_of_overlap

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.coordinate1 = Coordinate(x1, y1)
        self.coordinate2 = Coordinate(x2, y2)

    def width(self):
        return self.coordinate2.x - self.coordinate1.x
    
    def height(self):
        return self.coordinate2.y - self.coordinate1.y
        
    def area(self):
        return self.width * self.height
