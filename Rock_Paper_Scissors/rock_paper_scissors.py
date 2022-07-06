'''
Copyright (c) 2022 Angel Santana or one of its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Import Libraries
try:
    from os import (name, system)
    from time import(sleep)
    from random import (randint)
    
    print('[SUCCESSFULLY IMPORTED]')
except ImportError as ei:
    print(f'Import Library Error: {error}')
    
# Implement Clear function
def clear():
    if name == 'nt': # WINDOWS
        system('cls')
    
    if name == 'posix': # MAC/Linux
        system('clear')
        
# Implement Instructions
def rps_instructions():
    print(
        '''Instructions for RPS
    
    Rock BEATS Scissors
    Scissors BEATS Paper
    Paper BEATS Rock'''
    )

# Implement game logic
def rps():
    
    # Create Move Dictionary
    moves_dict = {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }
    # Create win-loss table
    RPS_WIN_TABLE = [
        [-1, 1, 0],
        [1, -1, 2],
        [0, 2, -1]
    ]
    
    while True:
        print('''Menu:
        Enter help for Instructions
        Enter Rock, Paper, or Scissors to begin playing
        Enter 3 to quit
        
        ''')
        
        
        user_input = input('Enter your move >> ').lower()
        
        
        if user_input == 'help':
            clear()
            rps_instructions()
            continue
        elif user_input == '3':
            clear()
            break
        elif user_input == 'rock':
            user_move = 0
        elif user_input == 'paper':
            user_move = 1
        elif user_input == 'scissors':
            user_move = 2
        else:
            clear()
            print('WRONG CHOICE')
            rps_instructions()
            continue
        
        # Computer Moves
        print('Computer making a move..')
        print('.')
        print('.')
        sleep(2)
        comp_move = randint(0, 2)
        
        print(f'Computer chose: {moves_dict[comp_move]}')
        
        # Decide Winner
        RPS_WINNER = RPS_WIN_TABLE[user_move][comp_move]
        
        if user_move == RPS_WINNER:
            print(f'{user_name} is the WINNER')
        elif comp_move == RPS_WINNER:
            print('COMPUTER is the WINNER')
        else:
            print('TIE GAME')
        
        
        # For dramatic effect
        print()
        sleep(2)
        clear()

# Run the game
if __name__ == '__main__':
    user_name = input('Enter your name\n>>')
    
    while True:
        print(
            '''Let's PLAY!
            Enter 1 to play Rock, Paper, Scissors
            Enter 2 to quit
            
            
        ''')
        
        try:
            user_choice = int(input('Enter your choice:\n>> '))
        except ValueError:
            clear()
            print('WRONG CHOICE')
            continue
        
        if user_choice == 1:
            rps()
        elif user_choice == 2:
            clear()
            print('Thanks for coming! Bye!')
            break
        else:
            clear()
            print('WRONG CHOICE. Read Instructions Carefully!')
        
# -----------------------------------------------------
# Follow me on Twitter @iamAngelSH
# Follow me on Github @iamAngelSH
# Connect with me on LinkedIn: Angel Santana Hernandez
# Subscribe to me on YT: Angel In Tech
# -----------------------------------------------------