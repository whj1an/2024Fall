import math
class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y ** 2))

    def up(self):
        self.move(0,1)

    def down(self):
        self.move(0,-1)

    def left(self):
        self.move(-1,0)

    def right(self):
        self.move(1,0)

    def get(self):
        return self.x, self.y
    
class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age = 0):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)

    def getAge(self):
        return self.age


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank



class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck


class BankAccount:
    def __init__(self, x = 0):
        self.x = float(x)

    def __repr__(self):
        return f'BankAccount({self.x:.1f})'

    def withdraw(self, w):
        self.x -= float(w)

    def deposit(self, d):
        self.x += float(d)

    def balance(self):
        return self.x

class PingPong:
    def __init__(self):
        self.s = True

    def next(self):
        if self.s:
            print('PING')
        else:
            print('PONG')
        self.s = not self.s

class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            pass

    def is_empty(self):
        return len(self.item) == 0

    def __repr__(self):
        """
        Returns a string representation of the Queue object.
        """
        return f"Queue({self.item})"

    def __len__(self):
        """
        Returns the number of items in the queue.
        """
        return len(self.item)

    def __eq__(self, other):
        """
        Compares two Queue objects for equality based on their items.
        """
        if isinstance(other, Queue):
            return self.item == other.item
        return False


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)#继承Point的__init__属性

    def __add__(self, other):
        """
        Adds two vectors
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            pass

    def __mul__(self, other):
        """
        dot product of two vectors.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Operands must be Vectors")

    def __repr__(self):
        """
        string representation to show "Vector" instead of "Point".
        """
        return f"Vector({self.x}, {self.y})"

class Marsupial:
    def __init__(self, color):
        """
        Initializes a Marsupial object with a specific color and an empty pouch.
        """
        self.color = color
        self.pouch = []

    def put_in_pouch(self, item):
        """
        Add
        """
        self.pouch.append(item)

    def pouch_contents(self):
        """
        Returns
        """
        return self.pouch

    def __repr__(self):
        """
        Returns a string
        """
        return f"I am a {self.color} Marsupial."

class Kangaroo(Marsupial):
    def __init__(self, color, x, y):
        """
        Extends the Marsupial constructor by adding x and y coordinates.
        """
        super().__init__(color)  # Call the Marsupial constructor
        self.x = x
        self.y = y

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"I am a {self.color} Kangaroo located at coordinates ({self.x}, {self.y})."


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

#***#
class Points:
    def __init__(self, points_list=None):
        """
        Initializes the Points object with a list of Point objects or an empty list if no input is given.
        """
        self.points = points_list if points_list is not None else []

    def add(self, x, y):
        """
        Adds a Point object with coordinates (x, y) to the list of points.
        """
        self.points.append(Point(x, y))

    def left_most_point(self):
        if not self.points:
            return None
        return min(self.points, key=lambda p: (p.x, p.y))

    def __len__(self):
        return len(self.points)

    def __repr__(self):
        return f"Points({self.points})"


print('---PE 5b---')
q1=Queue()
q1.enqueue('kiwi')
q1.enqueue('apple')
print(q1)


print('---PE 6---')
v1 = Vector(1, 3)
v2 = Vector(-2, 4)
print(v1 + v2)
print(v1 * v2)

print('---PE 7a---')
m = Marsupial("red")
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())
print(m)

print('---PE 7b---')
k = Kangaroo("blue", 0, 0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())
k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)
print(k)

print('---PE 8---')
a = [Point(1, 1), Point(1, 2), Point(2, 20), Point(1.5, -20)]
mypoints = Points(a)
mypoints.add(1, -1)
print(mypoints.left_most_point())
print(len(mypoints))
print(mypoints) 
