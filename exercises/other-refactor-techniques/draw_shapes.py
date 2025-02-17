# by Kami Bigdely
# Extract superclass.
class Shape:

    def display(self):
        if self.visible:
            print('drew the', self.name)
    
    def hide(self):
        self.visible = False

    def make_visible(self):
        self.visible = True

class Circle(Shape):
    
    def __init__(self, x, y, r, visible = True):
      self.name = 'circle'
      self.center_x = x
      self.center_y = y
      self.r = r
      self.visible = visible
        
    def get_center(self):
        return self.center_x, self.center_y
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, visible = True):
        # left-bottom corner.
        self.name = 'rectangle'
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.make_visible()
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())