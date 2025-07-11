import unittest
from range_expander import RangeExpander

class Testrangeexpander(unittest.TestCase):

    def test_stage1(self):
        expander=RangeExpander()
        result=expander.expand('1-3,5')
        assert result == [1,2,3,5]

    def test_stage2(self):
        expander=RangeExpander()
        result=expander.expand(" ,1-3, ,5")
        assert result == [1,2,3,5]


if __name__=='__main__':
    unittest.main()
    print('test_stage_basic  test cases passed')

