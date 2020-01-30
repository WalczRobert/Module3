#from format_output import average()
from format_output import average_scores

import unittest


class FunctionTestCase(unittest.TestCase):
    def test_average(self):
        list = [85, 90, 95]
        fname = input("What is your first name: ")
        lname = input("What is your last name: ")
        age = input("How old are you: ")
        print(1)
        self.assertEqual(list, average_scores.average(list))
        Print(2)
        assert average_score.average() == 90
        print(3)




'''class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        list = [88, 90, 95]
        fname = "Robert"
        lname = "Walczak"
        age = 45
       
        self.assertEqual(list, average_scores.average(list))
'''

if __name__ == '__main__':
    unittest.main()