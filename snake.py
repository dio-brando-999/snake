#This Class snake represents the snake. It will be responsible for the following:
#tracking the snake's position (stored as a list of tuples, which represent the coordinate of each body segement)
#handling movement (adding a new head and removing the tail given a boolean value representing if its eaten or not)
#changing direction (but preventing it from turning backward)
#detecting self-collisions (when it runs into itself) and detecting when it is out of bounds

class Snake:
    #__init__: Tuple Tuple -> None
    def __init__(self, start_pos, start_direction):
        self.body = [start_pos]
        self.direction = start_direction
    #move: Boolean -> None
    #updates a snakes 
    def move(self, ate_food) -> None:
        newHead=(self.body[0][0]+self.direction[0],self.body[0][1]+self.direction[1])
        self.body.insert(0, newHead)
        if not ate_food:
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
    #change_direction: Tuple[Int][Int] -> None
    #changes the direction given a tuple direction
    def change_direction(self, new_direction):
        if new_direction[0]==self.direction[0] and new_direction[0] == -self.direction[1]:
            return 
        else:
            self.direction = new_direction
    
    #check_out_of_bounds: Tuple[Int][Int] -> Boolean
    def check_out_of_bounds(self,world_size):
        head_x = self.body[0][0]
        head_y = self.body[0][1]
        width = world_size[0]
        height = world_size[1]
        return not (0 <= head_x < width and 0 <= head_y < height)