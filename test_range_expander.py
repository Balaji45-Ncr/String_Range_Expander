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

    def test_stage3_custom_delimiters(self):
        expander = RangeExpander(delimiters=['-', '..', 'to', '~'])
        result = expander.expand("1..3,4~6,10 to 12")
        assert result == [1, 2, 3, 4, 5, 6, 10, 11, 12]


if __name__=='__main__':
    unittest.main()
    print('test_stage_basic  test cases passed')

