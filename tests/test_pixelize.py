import unittest
import pixelize


class MyTestCase(unittest.TestCase):

    def test_make_matrix(self):
        rows, cols = pixelize.make_matrix(250, 383, 10)
        self.assertEqual(rows, 25)
        self.assertEqual(cols, 38)

    def test_average_color(self):
        colors = [(100, 100, 100, 255), (200, 200, 200, 255), (300, 300, 500, 255), (10000, 10000, 10000, 0)]
        result = pixelize.average_color(colors)
        print(result)


if __name__ == '__main__':
    unittest.main()
