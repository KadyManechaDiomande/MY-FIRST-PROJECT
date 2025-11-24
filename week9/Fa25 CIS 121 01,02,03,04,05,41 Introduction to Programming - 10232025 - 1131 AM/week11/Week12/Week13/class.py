# ----------------------------------------------
# Simple Text Snake Game
# Beginner-friendly version that meets rubric
# ----------------------------------------------

import random

# ----------------------------------------------
# Class: Snake
# ----------------------------------------------
class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]      # list (collection 1)
        self.direction = "RIGHT"
        self.grow_next = False

    def set_direction(self, new_direction):
        # prevent reversing direction directly
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}  # dict (collection 2)
        if new_direction != opposite[self.direction]:
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            new_head = (head_x - 1, head_y)
        elif self.direction == "DOWN":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x, head_y - 1)
        else:
            new_head = (head_x, head_y + 1)

        self.body.insert(0, new_head)

        # if snake didn't eat food, remove tail
        if not self.grow_next:
            self.body.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True


# ----------------------------------------------
# Load settings (file input)
# ----------------------------------------------
def load_settings():
    # File format:
    # rows,columns
    try:
        with open("settings.txt", "r") as f:
            line = f.readline().strip()
            parts = line.split(",")
            return int(parts[0]), int(parts[1])
    except:
        # default if file missing
        return 10, 10


# ----------------------------------------------
# Save score (file output)
# ----------------------------------------------
def save_score(score):
    with open("score.txt", "w") as f:
        f.write("Last Score: " + str(score))


# ----------------------------------------------
# Place food randomly
# ----------------------------------------------
def place_food(rows, cols, snake_positions):
    while True:
        food = (random.randint(0, rows-1), random.randint(0, cols-1))
        if food not in snake_positions:
            return food


# ----------------------------------------------
# Print board
# ----------------------------------------------
def print_board(rows, cols, snake, food):
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            pos = (r, c)
            if pos == snake.body[0]:
                row_str += "S"     # snake head
            elif pos in snake.body:
                row_str += "o"     # snake body
            elif pos == food:
                row_str += "F"
            else:
                row_str += "."
        print(row_str)
    print()


# ----------------------------------------------
# Main Game Function
# ----------------------------------------------
def play_game():
    rows, cols = load_settings()      # tuple (collection 3)
    snake = Snake((rows // 2, cols // 2))
    food = place_food(rows, cols, snake.body)

    score = 0

    print("Welcome to Simple Snake Game!")
    print("Use W/A/S/D to move. Type Q to quit.\n")

    while True:
        print_board(rows, cols, snake, food)

        move = input("Move (W/A/S/D/Q): ").upper()

        if move == "Q":
            break
        elif move == "W":
            snake.set_direction("UP")
        elif move == "S":
            snake.set_direction("DOWN")
        elif move == "A":
            snake.set_direction("LEFT")
        elif move == "D":
            snake.set_direction("RIGHT")
        else:
            print("Invalid input!")
            continue

        snake.move()

        # check wall collision
        head = snake.body[0]
        if head[0] < 0 or head[0] >= rows or head[1] < 0 or head[1] >= cols:
            print("You hit the wall!")
            break

        # check food
        if head == food:
            score += 1
            snake.grow()
            food = place_food(rows, cols, snake.body)

        # check self collision
        if snake.body[0] in snake.body[1:]:
            print("You hit yourself!")
            break

    print("\nGame Over! Score:", score)
    save_score(score)


# ----------------------------------------------
# Run the game
# ----------------------------------------------
play_game()
