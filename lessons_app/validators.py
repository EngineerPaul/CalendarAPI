import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.utils.representation import smart_repr
from CalendarApi.constraints import (
    С_morning_time, С_morning_time_markup, C_evening_time_markup,
    C_evening_time, C_salary_common, C_salary_high, C_salary_max, C_timedelta,
    C_datedelta
)


class AdminValidator():
    """ Сheck for non-intersection of lessons """

    def __init__(self, queryset):
        self.queryset = queryset
        self.message = "Some lesson is already scheduled for {} that day"

    def __call__(self, attrs):
        time = attrs['time']
        date = attrs['date']

        self.queryset = self.queryset.filter(date=date).values_list('time')
        times = [item[0] for item in self.queryset]

        for t1 in times:
            t2 = datetime.time(t1.hour+1, t1.minute, t1.second)
            if t1 <= time < t2:
                raise ValidationError(self.message.format(t1))

    def __repr__(self):
        return '<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        )


class UserValidator():
    """
    1. checking the overlap of lessons on each other - for all
    (lesson duration = 1 hour)
    2. check for too early and late lessons by day -  for users only
    3. checking for too early and late lessons by the hour - for users only
    4. checking cost of too early and late lessons by the hour - for users only
    5. checking the lead time - for users only
    (you can not add a lesson earlier than 6 hours)
    6. checking for cost limits (700<=salary) - for users only
    """

    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, attrs):
        salary = attrs['salary']
        time = attrs['time']
        date = attrs['date']
        dt_now = datetime.datetime.now()

        if salary < C_salary_common:
            raise ValidationError(
                f'The minimum cost of a lesson is {C_salary_common}'
            )
        elif salary > C_salary_max:
            raise ValidationError(
                f'Perfaps you made a mistake in the cost ({salary}₽)'
            )

        if date < dt_now.date():
            raise ValidationError(f"The date {date} has already arrived")
        elif date > (dt_now + C_datedelta).date():
            raise ValidationError(
                f"Please don't book a lesson earlier then {C_datedelta} "
                f"days in advace"
            )

        if datetime.datetime.combine(date, time) < dt_now + C_timedelta:
            raise ValidationError(
                f"Please, sign up for a lesson {C_timedelta} hours before to "
                f"start"
            )

        if time < С_morning_time:
            raise ValidationError(f"The time {time} is too early")
        elif С_morning_time <= time < С_morning_time_markup:
            if salary < C_salary_high:
                raise ValidationError(
                    f"in the morning ({С_morning_time}-{С_morning_time_markup}"
                    f" hours) the cost of the lesson is {C_salary_high}"
                )
        elif C_evening_time_markup <= time < C_evening_time:
            if salary < C_salary_high:
                raise ValidationError(
                    f"in the evening ({C_evening_time_markup}-{C_evening_time}"
                    f" hours) the cost of the lesson is {C_salary_high}"
                )
        elif time > C_evening_time:
            raise ValidationError(f"The time {time} is too late")

        self.queryset = self.queryset.filter(date=date).values_list('time')
        times = [item[0] for item in self.queryset]

        for t1 in times:
            t2 = datetime.time(t1.hour+1, t1.minute, t1.second)
            if t1 <= time < t2:
                raise ValidationError(
                    f"Some lesson is already scheduled for "
                    f"{t1} that day"
                )

    def __repr__(self):
        return '<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        )
