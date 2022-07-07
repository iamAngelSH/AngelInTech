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

try:
    from random import (
        choice
    )
    from string import (
        ascii_letters, 
        digits, 
        punctuation
    )
    print('[SUCCESSFULLY IMPORTED]')
    
except ImportError as ei:
    print(f'Import Library Error: {error}')
    
    
def ran_pw_gen(pw_length):
    all_chars = ascii_letters + digits + punctuation
    
    return ''.join(choice(all_chars) for i in range(pw_length))
    
    
if __name__ == '__main__':
    print(ascii_letters)
    print(digits)
    print(punctuation)
    
    
    for dl in [i for i in range(1,11)]:
        print(f'PW length of {dl}: {ran_pw_gen(dl)}')
        
    while True:
        try:
            user_length = abs(int(input('\nEnter Password length:\n>>')))
            print(f'\nYour password of length {user_length} is:\n{ran_pw_gen(user_length)}')
            break
        except ValueError:
            print('NOT A NUMBER')
            continue