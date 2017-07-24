from pyluach import dates

class Period(object):
    
    """
    A Period object represents a r'iya.

    Parameters
    ----------
    date : pyluach.dates.HebrewDate
    onah : string
      Must be either 'day' or 'night'
    haflaga : int, optional
      haflaga from the previous vest. Default is None.
    Attributes
    ----------
    date : pyluach.dates.HebrewDate
    onah : string
      'day or 'night'
    """

    def __init__(self, date, onah, haflaga=None):
        self.date = date
        if onah in ['day', 'night']:
            self.onah = onah
        else:
            raise ValueError("Onah has to have the value of either 'day' or "
                             "'night'")
        self.haflaga = haflaga
