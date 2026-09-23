""" 
    In a file called bank.py, implement a program that prompts the user for a greeting. 
    If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. 
    Otherwise, output $100. Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively. 
"""

def salutation(g):
    if g.startswith("hello"):
        return "$0"
    elif g.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    greeting = input("Greeting: ").lstrip().lower()
    print(salutation(greeting))

main()