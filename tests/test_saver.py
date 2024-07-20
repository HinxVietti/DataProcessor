import unittest
import pandas as pd
from data_processor.saver import DataSaver

class TestDataSaver(unittest.TestCase):
    def test_save_csv(self):
        saver = DataSaver()
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        saver.save_csv(df, 'tests/data/output.csv')
        saved_df = pd.read_csv('tests/data/output.csv')
        self.assertEqual(df.shape, saved_df.shape)

    def test_save_excel(self):
        saver = DataSaver()
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        saver.save_excel(df, 'tests/data/output.xlsx')
        saved_df = pd.read_excel('tests/data/output.xlsx')
        self.assertEqual(df.shape, saved_df.shape)
