import pytest

from pyluach.dates import HebrewDate
from vestos import reiya

class TestReiya(object):

    def test_invalid_onah(self):
        today = HebrewDate.today()
        for s in ['', 'wrong', None, 5]:
            with pytest.raises(ValueError):
                reiya.Reiya(today, s)
