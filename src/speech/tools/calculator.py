def isCalculus(text):
    words = text.split(' ')
    if words[0] == 'quanto' and words[1] == 'é':
        return True

def sum(text):
    words = text.split(' ')
    number_1 = int(words[2])
    operation = words[3]
    number_2 = int(words[4])

    result_str = ''

    if operation == '+':
        result = number_1 + number_2
        print(f"{number_1} + {number_2} = {result}")
        result_str = f"{number_1} + {number_2} = {result}"

    return result_str