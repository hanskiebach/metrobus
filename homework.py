import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = [value ** 2 for value in range(3,100, 3)]

    return return_value

if __name__ == "__main__":
    for x in squared_threes():
        print(x)