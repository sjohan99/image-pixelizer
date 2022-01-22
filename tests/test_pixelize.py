import unittest
import pixelize


class MyTestCase(unittest.TestCase):

    def test_get_rows_cols(self):
        rows, cols = pixelize.get_rows_cols(250, 383, 10)
        self.assertEqual(rows, 25)
        self.assertEqual(cols, 38)

    def test_average_color(self):
        colors = [(100, 100, 100, 255), (200, 200, 200, 255), (300, 300, 500, 255), (10000, 10000, 10000, 0)]
        result = pixelize.average_color(colors)
        self.assertEqual(result, (200, 200, 267, 255))


if __name__ == '__main__':
    unittest.main()
