import unittest
from click.testing import CliRunner
from bioinf_tools.seq_tools import nucleotide_counter, rev_complement


class test_seq_tools(unittest.TestCase):

    # Create a CliRunner instance, a Click utility, so that we can test what
    # happens for specific arguments from STDIN
    def setUp(self):
        self.runner = CliRunner()

    def Test_if_nucleotide_counter_returns_correct_list(self):
        """Test that nucleotide_counter returns the correct list."""
        result = self.runner.invoke(nucleotide_counter, input='-i AAACCGTT')

        self.assertEqual(result, [3, 2, 1, 2])

    def Test_if_rev_complement_returns_correct_string(self):
        """Test that rev_complement returns a reverse complement of a DNA sequence."""
        self.assertEqual(rev_complement('AAACCGTT'), 'AACGGTTT')


if __name__ == '__main__':
    unittest.main()
