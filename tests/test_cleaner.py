import unittest
import pandas as pd
from data_processor.cleaner import DataCleaner

class TestDataCleaner(unittest.TestCase):
    def test_clean_data(self):
        cleaner = DataCleaner()
        df = pd.DataFrame({
            'A': [1, 2, None],
            'B': [4, None, 6]
        })
        cleaned_df = cleaner.clean_data(df)
        self.assertEqual(cleaned_df.shape, (1, 2))
