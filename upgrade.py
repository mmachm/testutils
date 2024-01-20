from merge import merge


def enhance(cls):
    """
    A class decorator that gives two new assert methods, one with merge and one which just explicitly wraps assertEqual
    for convenience and cooperation with the override class decorator.

    :param cls:
    :return:
    """
    if not isinstance(cls, type):
        raise TypeError("Enhance is a class decorator, please apply it to a class.")

    try:
        assert callable(cls.assertEqual)
    except (AssertionError, AttributeError):
        raise ValueError("The class being enhanced had better have assertEqual implemented AND callable, "
                         "otherwise there is nothing to enhance.")
    class DecoratedClass(cls):
        def assertEqualMerged(self, *args):
            return cls.assertEqual(self, *merge(*args))

        def assertEqualNotMerged(self, *args):
            return cls.assertEqual(self, *args)

    return DecoratedClass


def override(cls):
    """
    A class decorator which overrides the assertEqual method to merge the expected and actual results first.
    To explicitly not merge them, use assertEqualNotMerged.

    :param cls:
    :return:
    """
    cls = enhance(cls)

    class DecoratedClass(cls):
        def assertEqual(self, *args):
            return cls.assertEqual(self, *merge(*args))

    return DecoratedClass
