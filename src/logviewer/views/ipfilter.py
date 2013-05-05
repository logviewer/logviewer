import filter


class IPFilter(filter.Filter):
    def __init__(self, ips): #ips is array
        self.ips = ips
