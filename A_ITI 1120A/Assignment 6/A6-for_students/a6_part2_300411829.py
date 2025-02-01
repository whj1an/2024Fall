class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'


class Rectangle:
    def __init__(self, bottom_left, top_right, color):
        '''
        (Rectangle, Point, Point, str) -> None
        Initialize and first point x < seconds' same 4 y
        '''
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color

    def get_bottom_left(self):
        return self.bottom_left

    def get_top_right(self):
        return self.top_right

    def get_color(self):
        return self.color

    def reset_color(self, color):
        self.color = color

    def move(self, dx, dy):
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def get_perimeter(self):
        return 2 * (self.top_right.x - self.bottom_left.x + self.top_right.y - self.bottom_left.y)

    def get_area(self):
        return (self.top_right.x - self.bottom_left.x) * (self.top_right.y - self.bottom_left.y)

    def intersects(self, other):
        a = (self.top_right.x < other.bottom_left.x or
             self.bottom_left.x > other.top_right.x or
             self.top_right.y < other.bottom_left.y or
             self.bottom_left.y > other.top_right.y)
        return not a

    def contains(self, x, y):
        return (self.bottom_left.x <= x <= self.top_right.x and
                self.bottom_left.y <= y <= self.top_right.y)

    def __repr__(self):
        ''' (Rectangle) -> str'''
        return f"Rectangle({repr(self.bottom_left)},{repr(self.top_right)},'{self.color}')"

    def __str__(self):
        ''' (Rectangle) -> str'''
        #print ?
        return (f"I am a {self.color} rectangle with bottom left corner at "
                f"({self.bottom_left.x}, {self.bottom_left.y}) and top right corner at "
                f"({self.top_right.x}, {self.top_right.y}).")

    def __eq__(self, other):
        ''' (Rectangle, Rectangle) -> bool'''
        return (self.bottom_left == other.bottom_left and
                self.top_right == other.top_right and
                self.color == other.color)

# create a list to store all the rectangles. find same part
class Canvas:
    def __init__(self):
        self.rectangle = []

    def add_one_rectangle(self, rectangle):
        """ (Canvas, Rectangle) -> None """
        self.rectangle.append(rectangle)

    def count_same_color(self, color):
        """ (Canvas, str) -> int
        count how many times each color appears in all rectangles"""
        count = 0
        for rectangle in self.rectangle:
            if rectangle.color == color:
                count += 1
        return count

    def total_perimeter(self):
        """(Canvas) -> int"""
        total = 0
        for rectangle in self.rectangle:
            total += rectangle.get_perimeter()
        return total

    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle
        find the smallest co-rectangle'''
        min_x = None
        max_x = None
        min_y = None
        max_y = None

        for rec in self.rectangle:
            if min_x is None or rec.bottom_left.x < min_x:
                min_x = rec.bottom_left.x

                # Update the maximum x coordinate
            if max_x is None or rec.top_right.x > max_x:
                max_x = rec.top_right.x

                # Update the minimum y coordinate
            if min_y is None or rec.bottom_left.y < min_y:
                min_y = rec.bottom_left.y

                # Update the maximum y coordinate
            if max_y is None or rec.top_right.y > max_y:
                max_y = rec.top_right.y

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), 'red')

    def common_point(self):
        '''(Canvas) -> bool
        Return T if there exists a point that intersects all rectangles on canvas'''
        if not self.rectangle:  # if it's not a rectangle, drop
            return False

        basic_rect = self.rectangle[0]

        for r in self.rectangle[1:]:
            if not basic_rect.intersects(r):
                return False

            # find the outside point
            bottom_left_x = max(basic_rect.bottom_left.x, r.bottom_left.x)
            bottom_left_y = max(basic_rect.bottom_left.y, r.bottom_left.y)
            top_right_x = min(basic_rect.top_right.x, r.top_right.x)
            top_right_y = max(basic_rect.top_right.y, r.top_right.y)

            # Rectangle(self, Point(x,y), Point(x,y), color)
            basic_rect = Rectangle(Point(bottom_left_x, bottom_left_y),Point(top_right_x, top_right_y),"red")

        return True

    def __len__(self):
        ''' (Canvas) -> int
        Return the number of rectangles on the canvas
        '''
        return len(self.rectangle)

    def __repr__(self):
        ''' (Canvas) -> str'''
        return f"Canvas({repr(self.rectangle)})"

    def __str__(self):
        ''' (Canvas) -> str
        user-friendly string representation'''
        return f"Canvas with {self.rectangle}."
