import random

class Snake:
    previously_occupied_square = [0, 1]

    def __init__(self, colour, head_colour, board, height, width):
        self.length = 1
        self.colour = colour
        self.head_colour = head_colour
        self.board = board
        self.head = BodyPart(self.board, head_colour, 0, 2)
        self.tail = self.head
        self.add_Block()
        self.previously_occupied_square = [0, 0]
        self.add_Block()
        self.previously_occupied_square=[]
        self.height = height
        self.width = width


    def add_Block(self):
        self.tail.next = BodyPart(self.board, self.colour,
                                  self.previously_occupied_square[0],
                                  self.previously_occupied_square[1])
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.length+=1
        self.previously_occupied_square = []


    def move(self, d):
        x=self.head.xcoord
        y=self.head.ycoord
        if d=='w':
            y-=1
        if d=='s':
            y+=1
        if d=='a':
            x-=1
        if d=='d':
            x+=1
        #Add new head forward
        #self.board.delete(self.head.tag)
        #temp = BodyPart(self.board, self.colour, self.head.xcoord, self.head.ycoord)
        #temp.next = self.head.next
        #self.head = temp
        temp = BodyPart(self.board, self.head_colour, x, y)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        self.board.delete(self.head.next.tag)
        self.head.next.tag = self.board.create_rectangle(29*self.head.next.xcoord+3,
                                                         29*self.head.next.ycoord+3,
                                                         29*self.head.next.xcoord+32,
                                                         29*self.head.next.ycoord+32,
                                                         outline="white", fill=self.colour)
        #Delete tail and add coords to previously occupied coords
        self.previously_occupied_square = [self.tail.xcoord, self.tail.ycoord]
        self.board.delete(self.tail.tag)
        self.tail = self.tail.prev
        self.tail.next = None

        temp = self.head
        temp = temp.next
        while temp is not None:
            if temp.__eq__(self.head):
                return -1
            temp = temp.next
        return 0


    def reset(self):
        temp = self.head
        while temp is not None:
            self.board.delete(temp.tag)
            if temp.prev is not None:
                del temp.prev
            temp = temp.next
        self.length = 1
        self.previously_occupied_square = [0, 1]
        self.head = BodyPart(self.board, self.head_colour, 0, 2)
        self.tail = self.head
        self.add_Block()
        self.previously_occupied_square = [0, 0]
        self.add_Block()
        self.previously_occupied_square = []



    def __str__(self):
        s = ""
        temp = self.head
        while temp is not None:
            s += temp.__str__()
            temp = temp.next
        return s



class BodyPart:
    def __init__(self, board, colour, xcoord, ycoord):
        self.colour = colour
        self.board = board
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.tag = self.board.create_rectangle(29*xcoord+3, 29*ycoord+3,
                                    29*xcoord+32, 29*ycoord+32, outline="white", fill=colour)
        self.next = None
        self.prev = None


    def __str__(self):
        return f'[{self.xcoord}, {self.ycoord}]'

    def __eq__(self, obj):
        if not isinstance(obj, BodyPart):
            return False
        if obj.xcoord != self.xcoord or obj.ycoord != self.ycoord:
            return False
        return True


class Food:
    def __init__(self, board, colour, width, height):
        self.colour = colour
        self.board = board
        self.width = width
        self.height = height
        self.restricted_squares={(0, 0), (0, 1), (0, 2)}
        self.x = random.randrange(2, 20)
        self.y = random.randrange(0, 20)
        self.tag = self.board.create_rectangle(
            29*self.x+3, 29*self.y+3, 29*self.x+32, 29*self.y+32, outline="#292e28", fill=colour)


    def reset(self):
        self.board.delete(self.tag)
        self.x = random.randrange(2, 20)
        self.y = random.randrange(0, 20)
        self.tag = self.board.create_rectangle(
            29 * self.x + 3, 29 * self.y + 3, 29 * self.x + 32, 29 * self.y + 32,
            outline="#292e28", fill=self.colour)
        while (self.x, self.y) in self.restricted_squares:
            self.reset()

    def reset_all(self):
        self.restricted_squares = {(0, 0), (0, 1), (0, 2)}
        self.reset()


