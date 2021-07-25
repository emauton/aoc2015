from aoc2015.core import dispatch


def test_dispatch_fail(capsys):
    '''Dispatch fails properly when passed a bad day'''
    # capsys is a pytest fixture that allows asserts agains stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    dispatch(['204'])
    captured = capsys.readouterr()
    assert 'No module named aoc2015.day204' in captured.out


def test_dispatch_day0(capsys):
    '''Dispatch to "template" day0 module works'''
    # capsys is a pytest fixture that allows asserts agains stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    dispatch(['0', 'arg1', 'arg2'])
    captured = capsys.readouterr()
    assert "day0: ['arg1', 'arg2']" in captured.out
