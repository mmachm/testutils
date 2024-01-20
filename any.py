
sentinel = object()

class Any:
    def __repr__(self):
        return "<ANY>"

    def __eq__(self, other):
        return True

ANY = Any()


class AnyOneThing:
    """
    I can think of a few usecases in our project at work, but overall I do not find this very useful.
    But it is fun to think about.
    """
    def __init__(self):
        self.matched = sentinel

    def __repr__(self):
        return f"<UnmatchedAnyOneThing>" if self.matched is sentinel else f"<AnyOneThing({str(self.matched)})>"

    def __eq__(self, other):
        if self.matched is sentinel:
            self.matched = other
            return True
        elif self.matched is self:  # this is here to prevent recursion
            return True
        return self.matched == other

