# FizzBuzzer Robot

This is a well known code Kata and it was implemented with TDD without a test framework. I'm using only Python's `assert` statement.

It's basically a robot which says:

* 'Fizz' when given number is multiple of 3
* 'Buzz' when given number is multiple of 5
* 'FizzBuzz' when given number is multiple of 3 and 5
* the given number, if it isn't multiple of 3 and/or 5


## Run tests
`$ python fizzbuzz.py`


## Usage

`>>> from fizzbuzz import robot`

`>>> robot(1) # '1'`

`>>> robot(3) # 'Fizz'`

`>>> robot(5) # 'Buzz'`

`>>> robot(15) # 'FizzBuzz'`
