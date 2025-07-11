from range_expander import RangeExpander


def test_stage1_basic():
    expander=RangeExpander()
    result=expander.expand('1-3,5')
    assert result == [1,2,3,5]