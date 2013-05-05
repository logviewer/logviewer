import filter


class DateFilter(filter.Filter):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
