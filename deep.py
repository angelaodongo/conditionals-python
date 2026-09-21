def answer(q):
    if q in ["42", "forty-two", "forty two"]:
        return "Yes"
    else:
        return "No"


def main():
    question = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    print(answer(question))

main()