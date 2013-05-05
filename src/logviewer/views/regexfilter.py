import filter


class RegexFilter(filter.Filter):
    def __init__(self, regex):
        self.regex = regex

