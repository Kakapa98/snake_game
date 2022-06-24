import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import math

def main_game(key,score,snake,food):
    """
        Main game by setting the controls and the window
    Args:
        key ([Key]): [The controls for the snake]
        score ([Integer]): [Keep track of the number of food snake consumes]
        snake ([String]): [Snake is the main string in the game]
        food ([String]): [This is the Food for the snake to grow big]
    """
    while key != 27:                                                  
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                
        win.addstr(0, 27, ' _KAKAPA_SNAKE_ ')                                   
        win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)          
        
        prevKey = key                                                 
        event = win.getch()
        key = key if event == -1 else event 


        if key == ord(' '):                                           
            key = -1                                                  
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:   
            key = prevKey

        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snake[0][0] == 0: snake[0][0] = 18
        if snake[0][1] == 0: snake[0][1] = 58
        if snake[0][0] == 19: snake[0][0] = 1
        if snake[0][1] == 59: snake[0][1] = 1

        # If snake runs over itself
        if snake[0] in snake[1:]: break

        if snake[0] == food:                                           
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 
                if food in snake: food = []
            win.addch(food[0], food[1], '*')
        else:    
            last = snake.pop()                                          
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '@')
        
    curses.endwin()
    print("\nScore - " + str(score))
    print("Thanks for Playing")


def config_game():
    """
        Setting up the game by designing the window
    """
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    return win,curses


def initialise_values(win, curses):
    """
        Definnign the Controls, score, snake and the food
    """
    key = KEY_RIGHT                                                
    score = 0

    snake = [[4,10], [4,9], [4,8]]                                    
    food = [10,20]                                                    

    win.addch(food[0], food[1], '*')  
    return key,score,snake,food                                


def welcome():
    """
        This is the welcome function for the Game 
    """
    print("<<<Welcome to Snake on the Terminal>>>")
    print("==================================================")
    numbers_ = [x * 5 for x in range(2000, 3000)]
    results = []

    while True:
        answer = input("Do you want to play Snake?: ")
        if answer.lower() == "no":
            print("There is always next Time!!!")
            exit()
        elif answer.lower() == "yes":
            print("[...Controls: Arrows(Up,Down,Left,Right),ESC - To exit the Game, SPACE - To Pause/Play...]")

            print("Loading...")
            for i, x in enumerate(numbers_):
                results.append(math.factorial(x))
                progress_bar(i + 1,len(numbers_))
            break
        else:
            continue 

def progress_bar(progress,total):
    percentage =  100 * (progress / float(total))
    bar = (('O' * int(percentage)) + ('=' * (100 - int(percentage))))
    print(f"\r|{bar}| {percentage:.2f}%", end="\r")


if __name__ == "__main__":

    welcome()
    win,curses = config_game()
    key,score,snake,food = initialise_values(win,curses)
    main_game(key,score,snake,food)