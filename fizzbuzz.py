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


if __name__ == '__main__':
    # numbers not multiple of 3 or 5
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    # multiples of 3, which turn to 'Fizz'
    assert robot(3) == 'Fizz'
    assert robot(6) == 'Fizz'
    assert robot(9) == 'Fizz'

    # multiples of 5, which turn to 'Buzz'
    assert robot(5) == 'Buzz'
    assert robot(10) == 'Buzz'
    assert robot(20) == 'Buzz'

    # multiples of 3 and 5, which turn to 'FizzBuzz'
    assert robot(15) == 'FizzBuzz'
    assert robot(30) == 'FizzBuzz'
    assert robot(45) == 'FizzBuzz'

    print('All tests passed!')
    print()
