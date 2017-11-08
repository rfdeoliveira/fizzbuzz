from functools import partial


multiple_of = lambda base, number: number % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(position):
    say = str(position)

    if multiple_of_3(position) and multiple_of_5(position):
        say = 'FizzBuzz'
    elif multiple_of_5(position):
        say = 'Buzz'
    elif multiple_of_3(position):
        say = 'Fizz'

    return say
