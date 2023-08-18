from datetime import datetime, timedelta


class DateBR:
    def __init__(self):
        self.registration_moment = datetime.today()

    def __str__(self):
        return self.format_data()

    def month_registration(self):
        months_of_the_year = [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december"
        ]
        month_regis = self.registration_moment.month
        return months_of_the_year[month_regis - 1]

    def day_week(self):
        day_week_list = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"
        ]
        day_week = self.registration_moment.weekday()
        return day_week_list[day_week]

    def format_data(self):
        formatted_data = self.registration_moment.strftime("%d/%m/%Y %H:%M")
        return formatted_data

    def time_register(self):
        time_regis = (datetime.today() + timedelta(days=30)) - \
            self.registration_moment
        return time_regis
