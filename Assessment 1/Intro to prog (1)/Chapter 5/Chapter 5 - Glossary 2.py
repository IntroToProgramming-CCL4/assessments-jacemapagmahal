glossary = {
    "variable": "is a way of storing values into the memory of the computer by using specific names that you define.",
    "string": "A sequence of characters, represented within single, double, or triple quotes in Python.",
    "dictionary": "A collection of key-value pairs, where each key is unique, used for storing data in an organized manner.
    "list": " a data structure in Python that is a mutable, or changeable, ordered sequence of elements.",
    "loop": "repeating something over and over until a particular condition is satisfied.",
}

glossary["function"] = "A block of code that performs a specific task and can be called by its name in the program."
glossary["script"] = "Is a dedicated document for writing Python code that you can execute."
glossary["method"] = "A function that is associated with an object and can be called on that object."
glossary["module"] = "A file containing Python code, which can define functions, classes, and variables."
glossary["argument"] = "A value or variable passed to a function or method when it is called."

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(meaning + "\n")
