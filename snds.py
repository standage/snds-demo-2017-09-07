def sums(values):
    """
    Given a list of numbers `values`, return a list of the sums of each non-
    decreasing sub-list. For example, if `values = [1, 2, 3, 3, 1, 5, 6, 3, 1,
    2, 3]`, the output should be `[9, 12, 3, 6]`. 
    """
    if len(values) == 0:
        return []
    sumlist = list()
    
    buffer = list()
    for value in values:
        if len(buffer) > 0 and value < buffer[-1]:
            newsum = sum(buffer)
            sumlist.append(newsum)
            buffer = list()
        buffer.append(value)
    newsum = sum(buffer)
    sumlist.append(newsum)
    
    return sumlist


def test_all_values_decreasing():
    assert sums([9,8,7,6,5,4,3,2,1]) == [9,8,7,6,5,4,3,2,1]

def test_empty():
    assert sums([]) == []

def test_zero():
    assert sums([0]) == [0]

def test_example():
    assert sums([1, 2, 3, 3, 1, 5, 6, 3, 1, 2, 3]) == [9, 12, 3, 6]

def test_single_value():
    assert sums([5] * 25) == [125]

def test_negative_values():
    assert sums([-3, -2, -1, -2, -3]) == [-6, -2, -3]
