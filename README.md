# FizzBuzzer Robot

This is a well known code Kata and it was implemented with TDD using [unittest](https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest), Python's Unit Testing Framework, inspired by [JUnit](http://junit.org/).

It's basically a robot which says:

* 'Fizz' when the given number is multiple of 3
* 'Buzz' when the given number is multiple of 5
* 'FizzBuzz' when the given number is multiple of 3 and 5
* the given number, if it isn't multiple of 3 and/or 5


## Run tests
`$ python -m unittest`


## Usage

`$ python`

`>>> from fizzbuzz import robot`

`>>> robot(1)  # outputs: '1'`

`>>> robot(3)  # outputs: 'Fizz'`

`>>> robot(5)  # outputs: 'Buzz'`

`>>> robot(15)  # outputs: 'FizzBuzz'`
