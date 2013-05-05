import filter


class ServiceFilter(filter.Filter):
    def __init__(self,service):
        self.service = service

