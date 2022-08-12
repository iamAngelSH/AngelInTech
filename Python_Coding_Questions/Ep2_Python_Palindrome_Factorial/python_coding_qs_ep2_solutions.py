import re
class Palindrome:
    '''When init the class Palindrome, we will always expect to pass in a string'''
    def __init__(self, string):
        '''Convert string to lowercase to make things easier to deal with
           Create a variable to hold our palindrome string to compare'''
        self.s = string.lower()
        self.palindrome_string = ''
    
    def only_words_from_string(self, string):
        '''Helper function
            - Find only words in our string using RE library (Regular Expressions)
            
            NOTICE THAT THE WORDS ARE JOINED TOGETHER, 
            IF THERE IS A SPACE, THEN SOME PALINDROMES WON'T BE ACCOUNTED FOR 
        '''
        
        return ''.join(re.findall(r'\w+', string))
    
    def isPalindrome(self):
        '''Our Palindrome Function
        - Call our helper function
        - Add each character from our word into our palindrome string
        - If our palindrome string and word equal each other, return true
        - Return False other wise'''
        word = self.only_words_from_string(self.s)
        
        for i in word: ## Add each character in word to our empty palindrome string
            self.palindrome_string = i + self.palindrome_string


        # Check if word and string are the same
        return (
            f'[{word}] is a Palindrome --> {self.palindrome_string}' if word == self.palindrome_string 
            else f'[{word}] is Not a Palindrome: {self.palindrome_string}' 
        )
            

class Factorial:
    '''When initializing the class Factorial, we will always expect to pass in a number'''
    def __init__(self, integer):
        '''We will add 1 to our integer value to be able to include the full result of the number'''
        self.num = integer + 1
        self.base_cases = [0, 1] # Memoization, covers the base case of Factorial(0 or 1) to return 1
    
    def calcRecur(self):
        '''- Check for our base cases
           - If not a base case, decrease number, 
           iterate from starting number and multiply with next'''
        if self.num in self.base_cases: return 1
        else:
            self.num -= 1
            return self.num * self.calcRecur()
        
def main():
    print('Palindrome Test')
    for string in [
                    'mom', 'dad', 'stanley yelnats', 
                    '1 tot !', "A man, a plan, a canal: Panama", 
                    "@# Computer Science Portal.!!!", 'malayalam',
                    'Python is so much fun'
        ]:
        print(Palindrome(string).isPalindrome())
        
    print('\n************************\nFactorial Test')
    for i in range(0, 10):
        print(f'Factorial of {i} --> {Factorial(i).calcRecur()}')
        
if __name__ == "__main__":
    main()