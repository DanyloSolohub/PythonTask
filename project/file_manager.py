import json
from datetime import datetime


class FileManager:

    @staticmethod
    def save_holidays_to_file(country_code, holidays, start_date, end_date):
        filename = (
            f'{country_code}_actual_result.txt'
        )
        with open(filename, 'w+') as file:
            for holiday in holidays:
                file.write(json.dumps(holiday) + '\n')
