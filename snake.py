class Snake:
    #__init__: Tuple Tuple -> None
    def __init__(self, start_pos, start_direction):
        self.body = [start_pos]
        self.direction = start_direction
    #move: None -> None
    #updates a snakes 
    def move(self) -> None:
        newHead=(self.body[0][0]+self.direction[0],self.body[0][1]+self.direction[1])
        self.body.insert(0, newHead)
        self.body.pop()
    
    #check_for_collison: None -> Boolean
    #checks the snake if it has collided with itself or not
    #returns true if it has collided, else: false
    def check_for_collison(self) -> bool:
        head = self.body[0] 
        body_positions = set(self.body[1:])
        if head in body_positions:
            return True
        else:
            return False

    
snake1 = Snake((10,10), (0, -1))
snake2 = Snake((5,5), (0, -1))

snake1.body.append((11,10))
print("Snake 1 Body,:", snake1.body)
print("Snake 2 Body,:", snake2.body)
#This Class snake represents the snake. It will be responsible for the following:
#Tracking the snake's position (stored as a list of tuples).
#Handling movement (adding a new head and removing the tail).
#Changing direction (but preventing it from turning backward).
#Detecting self-collisions (when it runs into itself).
#Growing when it eats food.
    #def move(self):
