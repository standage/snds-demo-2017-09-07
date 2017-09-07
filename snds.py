def sums(values):
    """
    Given a list of numbers `values`, return a list of the sums of each non-
    decreasing sub-list. For example, if `values = [1, 2, 3, 3, 1, 5, 6, 3, 1,
    2, 3]`, the output should be `[9, 12, 3, 6]`.
    """
    pass

def test_empty():
    assert sums([]) == []

def test_example1():
    assert sums([1, 2, 3, 3, 1, 5, 6, 3, 1, 2, 3]) == [9, 12, 3, 6]

def test_zero():
    assert sums([0]) == [0]

def test_single_value():
    assert sums([5]* 25) == [125]

def test_negative_value():
    assert sums([-5]* 25) == [125]
