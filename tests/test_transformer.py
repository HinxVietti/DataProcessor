import unittest
import pandas as pd
from data_processor.transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    def test_transform_data(self):
        transformer = DataTransformer()
        df = pd.DataFrame({
            'old_column': [1, 2, 3]
        })
        transformed_df = transformer.transform_data(df)
        self.assertEqual(transformed_df['new_column'].tolist(), [2, 4, 6])
