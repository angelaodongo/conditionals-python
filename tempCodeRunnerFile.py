def salutation(g):
    if g == "hello":
        return "$0"
    elif g.startswith("h") and g != "hello":
        return "$20"
    else:
        return "$100"


def main():
    greeting = input("Greeting: ").lstrip().lower()
    print(salutation(greeting))

main()