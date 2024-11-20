import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="Exercise_logging_2.log",
    filemode="w"
)

def sum_of_numbers(*num):
    logging.info(f"The sum of numbers {num} is: {sum(num)}")
    return sum(num)


import math

def square_root(num:int):
    try:
        math.sqrt(num)
        logging.info(f"Square root of number: {num} is: {math.sqrt(num):.2f} ")
        return math.sqrt(num)
    except TypeError as err:
        logging.error("Number is not a integer!")
        return "Error: cannot calculate square root"


def num_of_characters(words):
    logging.info(f"Number of characters in sentence: '{words}' are: {len(words)}")
    return len(words)


def division(x:int, y:int):
    try:
        answer = x / y
        logging.info(f"Division of numbers {x} and {y} is {answer:.2f}")
        return answer
    except ZeroDivisionError as err:
        logging.error("Cannot divide by 0")
        return "Error: cannot divide by 0"


print(sum_of_numbers(10, 20, 30))
print(square_root(16))
print(square_root("sixteen"))
print(num_of_characters("Python logging is useful"))
print(division(10, 2))
print(division(10, 0))

