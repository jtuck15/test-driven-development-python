def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} should not contain {1}".format(collection, item)
    
def test_between(lower_limit, upper_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)


# test to fail test_are_equal()
# test_are_equal(number_of_evens([1, 2, 3, 4]), 2)

# test to fail test_not_equal()    
# test_not_equal(1, 1)

# test to fail test_is_in()
# test_is_in([1, 2, 3, 4], 7)

# test to fail test_not_in()
# test_not_in([1, 2, 3], 3)

# test to fail test_between()
# test_between(1, 7, 13)