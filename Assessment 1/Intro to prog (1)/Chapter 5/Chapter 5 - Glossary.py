
glossary = {
    "variable": "A container that holds data which can be changed during the execution of a program.",
    "function": "A block of code that performs a specific task and can be called by its name in the program.",
    "loop": "A control structure used for repeatedly executing a set of statements until a certain condition is met.",
    "list": "An ordered collection of items, which can be of different types, enclosed in square brackets [] in Python.",
    "dictionary": "A collection of key-value pairs, where each key is unique, used for storing data in an organized manner."
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(meaning + "\n")
