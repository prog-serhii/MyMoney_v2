def date_range(self, start_date, end_date):
    # a model must contain a date field - date
    return self.filter(date__range=(start_date, end_date))
