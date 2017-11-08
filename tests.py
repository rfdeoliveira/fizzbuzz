from unittest import TestCase
from fizzbuzz import robot


class FizzBuzzTest(TestCase):
    # say number when it isn't multiple of 3 or 5
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    # say 'Fizz' when number is multiple of 3
    def test_when_3_say_Fizz(self):
        self.assertEqual(robot(3), 'Fizz')

    def test_when_6_say_Fizz(self):
        self.assertEqual(robot(6), 'Fizz')

    def test_when_9_say_Fizz(self):
        self.assertEqual(robot(9), 'Fizz')

    # say 'Buzz' when number is multiple of 5
    def test_when_5_say_Buzz(self):
        self.assertEqual(robot(5), 'Buzz')

    def test_when_10_say_Buzz(self):
        self.assertEqual(robot(10), 'Buzz')

    def test_when_20_say_Buzz(self):
        self.assertEqual(robot(20), 'Buzz')

    # say 'FizzBuzz' when number is multiple of 3 and 5
    def test_when_15_say_FizzBuzz(self):
        self.assertEqual(robot(15), 'FizzBuzz')

    def test_when_30_say_FizzBuzz(self):
        self.assertEqual(robot(30), 'FizzBuzz')

    def test_when_45_say_FizzBuzz(self):
        self.assertEqual(robot(45), 'FizzBuzz')
