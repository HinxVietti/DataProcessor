import unittest
from data_processor.reader import DataReader

class TestDataReader(unittest.TestCase):
    def test_read_csv(self):
        reader = DataReader()
        df = reader.read_csv('tests/data/test.csv')
        self.assertEqual(df.shape, (3, 4))

    def test_read_excel(self):
        reader = DataReader()
        df = reader.read_excel('tests/data/test.xlsx')
        self.assertEqual(df.shape, (3, 4))
