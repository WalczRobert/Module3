#from format_output import average()
from format_output import average_scores

import unittest


class FunctionTestCase(unittest.TestCase):
    def test_average(self):
        list = [85, 90, 95]
        fname = 'Robert'
        lname = 'Edward'
        age = 31
        print(1)
        self.assertEqual(90, average_scores.average(list, lname, fname, age))
        


if __name__ == '__main__':
    unittest.main()
