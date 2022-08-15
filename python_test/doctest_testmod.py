def test_funtion(n):
    if n > 0 :
        return 1
    if n < 0 :
        return -1
    if n == 0 :
        return 0

def main():
    """
    >>> test_funtion(5)
    1
    >>> test_funtion(30)
    1
    >>> test_funtion(-30)
    -1
    >>> test_funtion(0)
    0
    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()