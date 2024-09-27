import math


"""
point class
circle class'
rectangle
"""

##example changes to commit 

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        
        self.y = y

    def print_point(self):
        """Print a Point object in human-readable format."""
        print('(%g, %g)' % (self.x, self.y))

    def move_point(self,dx,dy):
        """
        Input coordinates to add/sub to existing point to move in 2D space
        :param dx: +/- n to add to x coord
        :param dy: +/- n to add to y coord
        :return: no return
        """
        self.x += dx
        self.y += dy

class Circle:
    """Represents a rectangle.

    attributes: center, radius.
    """
    def __init__(self, center=None, radius = 0):
        self.center = center if center else Point()
        self.radius = radius

    def __add__(self, other):
        self.radius += other.radius

    def find_center(self):
        """Returns a Point at the center of a Rectangle.

        returns: new Point
        """
        return self.center

    def move_center(self,dx,dy):
        """
        use Point's move_point method to move the center point
        """
        if self.center: self.center.move_point(dx,dy)

    def grow_circle(self, dradius):
        """Modifies the Rectangle by adding to its width and height.

        dwidth: change in width (can be negative).
        dheight: change in height (can be negative).
        """
        self.radius += dradius

    def scale_circle(self, scale_factor):
        """Scale the Rectangle by modifying its width and height values by multiplying by the scale_factor
        :param scale_factor: factor to multiply height and width
        """
        self.radius *= scale_factor

    def point_in_circle(self,point):

        if not isinstance(point,point):
            raise TypeError("point must be an instance of the Point class")

        dist = math.sqrt((self.center.x - point.x)**2 + (self.center.y - point.y)**2)
        return dist <= self.radius

    def rect_in_circle(self,rectangle):
        """
        Take a rectangle object and return true if all of its four corners lie within or
        on the circle object
        :param rectangle: an object using the Rectangle class
        :return: True if Rectangle in Circle else False
        """
        b_l = rectangle.corner
        b_r = Point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
        t_l = Point(rectangle.corner.x,rectangle.corner.y + rectangle.height)
        t_r = Point(rectangle.corner.x + rectangle.width,rectangle.corner.y + rectangle.height)

        return (self.point_in_circle(b_l) and
                self.point_in_circle(b_r) and
                self.point_in_circle(t_l) and
                self.point_in_circle(t_r))
    def rect_circle_overlap(self,rectangle):
        """
        Take a rectangle object and return true if any of its four corners lie within or
        on the circle object
        :param rectangle: an object using the Rectangle class
        :return: True if Rectangle in Circle else False
        """
        b_l = rectangle.corner
        b_r = Point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
        t_l = Point(rectangle.corner.x,rectangle.corner.y + rectangle.height)
        t_r = Point(rectangle.corner.x + rectangle.width,rectangle.corner.y + rectangle.height)

        return (self.point_in_circle(b_l) or
                self.point_in_circle(b_r) or
                self.point_in_circle(t_l) or
                self.point_in_circle(t_r))

class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """
    def __init__(self, width=0, height=0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner if corner is not None else Point()

    def find_center(self):
        """Returns a Point at the center of a Rectangle.

        returns: new Point
        """
        p = Point()
        p.x = self.corner.x + self.width / 2.0
        p.y = self.corner.y + self.height / 2.0
        return p

    def grow_rectangle(self, dwidth, dheight):
        """Modifies the Rectangle by adding to its width and height.

        dwidth: change in width (can be negative).
        dheight: change in height (can be negative).
        """
        self.width += dwidth
        self.height += dheight

    def scale_rectangle(self, scale_factor):
        """Scale the Rectangle by modifying its width and height values by multiplying by the scale_factor

        :param scale_factor: factor to multiply height and width
        """
        self.width *= scale_factor
        self.height *= scale_factor

def main():
    first_pt = Point(0,0)
    first_pt.print_point()
    first_pt.move_point(2,2)
    first_pt.print_point()

    """
    circle1
    circle2
    
    circle1 + circle2
    circle1.radius + circle2.radius =
    
    """

if __name__ == '__main__':
    main()
