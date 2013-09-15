class EvenException(Exception):
    """
    EvenException is raised when a position or size is even when
    it shouldn't be.
    """

class InvalidSizeException(Exception):
    """
    InvalidSizeException is raised when the size is invalid.
    Invalid can mean as Example too small or not a list, tuple or integer.
    """