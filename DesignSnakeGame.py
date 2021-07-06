# TC: O(N x M) where N os the height of the screen size and M is the width of the screen size. In worst case, the snake can be size of the whole screen.
# SC: O(N) where N is the maximum size of the snake achieved.

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
#         linked list for snake
        self.snake = []
        self.snakeHead = (0,0)
        self.snake.append(self.snakeHead)
        self.food = food
        self.height = height
        self.width = width

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
#         moving in directions
        if direction == "U": 
            coord = self.snakeHead[0]
            coord -= 1
            self.snakeHead = (coord, self.snakeHead[1])
        if direction == "L": 
            coord = self.snakeHead[1]
            coord -= 1
            self.snakeHead = (self.snakeHead[0], coord)
        if direction == "R": 
            coord = self.snakeHead[1]
            coord += 1
            self.snakeHead = (self.snakeHead[0], coord)
        if direction == "D": 
            coord = self.snakeHead[0]
            coord += 1
            self.snakeHead = (coord, self.snakeHead[1])
    
#       if snake hits the boundary
        if  self.snakeHead[0] < 0 or self.snakeHead[0] >= self.height or self.snakeHead[1] < 0 or self.snakeHead[1] >= self.width: 
            return -1
    
#       if snake eats itself
        for i in range(1, len(self.snake)):
            x, y = self.snake[i]
            if x == self.snakeHead[0] and y == self.snakeHead[1]: 
                return -1
        
#        if snake eats food
        if len(self.food) > 0:
            currFood_x, currFood_y = self.food[0]
            if currFood_x == self.snakeHead[0] and currFood_y == self.snakeHead[1]: 
                self.snake.append(self.food.pop(0))
                return len(self.snake) - 1
        
#         normal move
        self.snake.pop(0)
        self.snake.append((self.snakeHead[0], self.snakeHead[1]))
        return len(self.snake) - 1
    
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
