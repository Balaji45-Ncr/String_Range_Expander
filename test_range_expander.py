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

    def test_stage4_reversed_and_invalid(self):
        expander = RangeExpander(['-', '..', 'to', '~'])
        assert expander.expand("5-3,3-3,2") == [5, 4, 3, 3, 2]

        try:
            expander.expand("3-a")
            assert False, "Expected ValueError"
        except ValueError:
            pass

    def test_stage5_step_values(self):
        expander = RangeExpander(delimiters=['-'], step_delimiter=':')
        self.assertEqual(expander.expand("1-10:2"), [1, 3, 5, 7, 9])
        self.assertEqual(expander.expand("10-1:3"), [10, 7, 4, 1])


if __name__=='__main__':
    unittest.main()
    print('test_stage_basic  test cases passed')

