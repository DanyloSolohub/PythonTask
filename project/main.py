from datetime import datetime
from holiday_service import HolidayService
from file_manager import FileManager
import pytz

utc = pytz.UTC


def main():
    countries_list = ['ua', 'us', 'gb']
    start_time = datetime(year=1992, month=7, day=7, tzinfo=utc)
    end_time = datetime(year=1992, month=9, day=18, tzinfo=utc)

    holiday_service = HolidayService()

    for country in countries_list:
        holidays = holiday_service.get_holidays_for_country(country, start_time, end_time)
        FileManager.save_holidays_to_file(country, holidays, start_time, end_time)


if __name__ == "__main__":
    main()
