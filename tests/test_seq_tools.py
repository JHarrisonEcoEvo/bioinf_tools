import unittest
from bioinf_tools.seq_tools.nucleotide_counter import nucleotide_counter
from bioinf_tools.seq_tools.rev_complement import rev_complement


# Usage: python -m unittest tests/test_seq_tools.py

class test_seq_tools(unittest.TestCase):
    # Remember that test functions need to start with "test" in order for unittest to recognize them.
    def test_if_nucleotide_counter_returns_correct_list(self):
        """Test that nucleotide_counter returns the correct list."""
        self.assertEqual(nucleotide_counter('AAACCGTT'), [3, 2, 1, 2])

    def test_if_rev_complement_returns_correct_string(self):
        """Test that rev_complement returns a reverse complement of a DNA sequence."""
        self.assertEqual(rev_complement('AAACCGTT'), 'AACGGTTT')




if __name__ == '__main__':
    unittest.main()
