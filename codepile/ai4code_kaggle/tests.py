## Test Topcoder Crawling
import os
import pandas as pd
from ai4code_kaggle import AI4Code_Kaggle

import os
import pandas as pd
from ai4code_kaggle import AI4Code_Kaggle

from unittest import TestCase
class TestAI4CodeDataset(TestCase):

    def setUp(self):
            
        # make directory if not exists
        if not os.path.exists('data'):
            os.mkdir('data')
        ai4code_dataset = AI4Code_Kaggle("data/", "data/")
        ai4code_dataset.download()

        self.dummy = pd.read_parquet("test/ai4code_kaggle_dummy.parquet")
        self.df = pd.read_parquet("data/AI4Code_Kaggle.parquet")

    def test_same_cols(self):
        self.setUp()
        self.assertEqual(self.dummy.columns.tolist(), self.df.columns.tolist())

if __name__ == '__main__':
    TestAI4CodeDataset().test_same_cols()