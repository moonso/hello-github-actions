from actions.code import convert_number


def test_convert_int():
    # GIVEN an integer
    a = 1
    # WHEN converting the integer
    res = convert_number(a)
    # THEN assert a integer is returned
    assert isinstance(res, int)
