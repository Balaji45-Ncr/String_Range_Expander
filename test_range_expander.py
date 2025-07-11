import unittest
from range_expander import RangeExpander

class Testrangeexpander(unittest.TestCase):
    def test_stage1_basic(self):
        expander=RangeExpander()
        result=expander.expand("1-3,5")
        assert result == [1,2,3,5]


if __name__=='__main__':
    unittest.main()
    print('test_stage2_basic  test cases passed')

