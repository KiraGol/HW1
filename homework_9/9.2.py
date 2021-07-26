from datetime import datetime, timedelta


def week_ago():
    """returns a date a week ago from the current point in time"""
    past_date = datetime.now() - timedelta(days=7)
    return past_date


print(week_ago())
