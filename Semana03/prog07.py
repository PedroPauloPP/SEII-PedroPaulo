def hello_func(greeting):
	return '{} Function.'.format(greeting)

print(hello_func('Hi'))


def students_info(*args, **kwargs):
	print(args)
	print(**kwargs)
	
students_info(*courses, **info)

courses = ['Math','Art']
info = {'name': 'PedroPaulo', 'age':28}
	
 
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Retorna verdadeiro para anos bissextos e falso para anos não bissextos."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """retorna o numero de dias no mes daquele ano."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))