def answer(q):
    if q == "42":
        return "Yes"
    elif q == "forty-two":
        return "Yes"
    elif q == "forty two":
        return "Yes"
    else:
        return "No"


def main():
    question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    print(answer(question))

main()