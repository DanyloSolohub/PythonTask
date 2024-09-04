import os
from datetime import datetime, timezone

import requests

import pytz
from dotenv import load_dotenv

load_dotenv()
utc = pytz.UTC


class HolidayService:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('CALENDARIFIC_API_KEY')
        self.base_url = 'https://calendarific.com/api/v2/holidays'

    def get_holidays_for_country(self, country_code: str, start_date: datetime, end_date: datetime):
        holidays = []
        for year in range(start_date.year, end_date.year + 1):
            holidays.extend(self._get_holidays_for_year(country_code, year, start_date, end_date))
        return holidays

    def _get_holidays_for_year(self, country_code: str, year: int, start_date: datetime, end_date: datetime):
        params = {
            'api_key': self.api_key,
            'country': country_code,
            'year': year,
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return self._filter_holidays(data['response']['holidays'], start_date, end_date)

    @classmethod
    def _filter_holidays(cls, holidays, start_date: datetime, end_date: datetime):
        filtered_holidays = []
        for holiday in holidays:
            holiday_date = datetime.fromisoformat(holiday['date']['iso']).replace(tzinfo=utc)
            if start_date <= holiday_date <= end_date:
                filtered_holidays.append(holiday)
        return filtered_holidays
