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


def assert_equal(actual, expected):
    from sys import _getframe
    msg = 'Line {} failed! got "{}" expecting "{}"'

    if not actual == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, actual, expected))


if __name__ == '__main__':
    # numbers not multiple of 3 or 5
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    # multiples of 3, which turn to 'Fizz'
    assert_equal(robot(3), 'Fizz')
    assert_equal(robot(6), 'Fizz')
    assert_equal(robot(9), 'Fizz')

    # multiples of 5, which turn to 'Buzz'
    assert_equal(robot(5), 'Buzz')
    assert_equal(robot(10), 'Buzz')
    assert_equal(robot(20), 'Buzz')

    # multiples of 3 and 5, which turn to 'FizzBuzz'
    assert_equal(robot(15), 'FizzBuzz')
    assert_equal(robot(30), 'FizzBuzz')
    assert_equal(robot(45), 'FizzBuzz')
