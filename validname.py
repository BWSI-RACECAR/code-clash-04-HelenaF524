"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #4 - Validate Name (validname.py)


Author: Wonjun Lee

Difficulty Level: 3/10

Prompt: Bill is trying to come up with a name for his RACECAR, but he wants to name his 
car so that there are no duplicate characters in the name. Please write a function that 
returns whether a given string input is a valid name or not. 

Constraints: Inputs will consist of only alphanumeric characters. Lowercase and uppercase
characters are considered different. The length of string will be in the range [0, 100] inclusive.

Test Cases:
Input: “AaBbCc1234”     Output: True 
Input: “Aa123a”         Output: False
Input: “qwer12341”      Output: False
"""
from collections import Counter
from re import L

class Solution:
    def validateName(self,input):
        # type input: string
        # return: bool
            
        # TODO: Write code below to return a bool with the solution to the prompt
        c = Counter()
        letters = []
        for i in range(len(input)):
            letters.append(input[i:i+1])
        for let in letters:
            c[let]+=1
        for i in c.values():
            if i>1:
                return False
        return True

def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.validateName(string1)
    print(ans)

if __name__ == "__main__":
    main()