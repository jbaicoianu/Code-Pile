from unittest import TestCase

import os
import pandas as pd
from codepile.codepile import Config
from codepile.leetcode.leetcode import LeetCodeDataset

import pytest

class TestLeetCodeDataset(TestCase):
    @pytest.mark.s3_download
    def test_same_cols(self):
        if not os.path.exists('data/'):
            os.mkdir('data/')

        config = Config(
            raw_data_dir="data/",
            output_data_dir="data/",
            tmpdir="/tmp"
        )

        lc_dataset = LeetCodeDataset(config)
        lc_dataset.download()

        self.dummy = pd.read_parquet("test/leetcode_dummy.parquet")
        self.df = pd.read_parquet("data/leetcode_topics_with_questions.parquet.gzip")
        self.assertEqual(self.dummy.columns.tolist(), self.df.columns.tolist())