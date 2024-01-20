import re


class Rex:
    """
    This is a combination of regex and ANY

    """
    def __init__(self, pattern):
        self.pattern = pattern

    def __eq__(self, other):
        if not (isinstance(other, str)) or isinstance(other, Rex):
            return NotImplemented
        if isinstance(other, str):
            m = re.match(self.pattern, other)
            if m and m.group(0) == other:
                return True
            return False
        else:
            return self.pattern == other.pattern

    def __str__(self):
        return self.pattern

    def __repr__(self):
        return f"<Rex({self.pattern})>"
