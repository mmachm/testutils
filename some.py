class SOME:
    def __init__(self, _type):
        if not isinstance(_type, type):
            raise TypeError("SOME can only accept classes to compare.")
        self._type = _type

    def __eq__(self, other):
        if isinstance(other, SOME):
            return self._type == other._type
        elif isinstance(other, self._type):
            return True
        else:
            return NotImplemented

    def __repr__(self):
        return f"<SOME {str(self._type.__name__)}>"
