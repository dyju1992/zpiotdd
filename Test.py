__author__ = 'dyju'

import unittest
import zad2

class Test_Fibonacci(unittest.TestCase):

    def test_Fib(self):
        self.assertEqual(zad2.Wynik[6], 13)

    def test_Fib_sum(self):
        self.assertEqual(zad2.suma, 4613732)



suite = unittest.TestLoader().loadTestsFromTestCase(Test_Fibonacci)
unittest.TextTestRunner(verbosity=2).run(suite)