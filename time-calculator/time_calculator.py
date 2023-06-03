def add_time(start, duration, start_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    new_minute = start_minute + duration_minute
    carry_hour = new_minute // 60
    new_minute %= 60

    new_hour = start_hour + duration_hour + carry_hour
    carry_day = new_hour // 12
    new_hour %= 12

    if period == "PM":
        carry_day += 1

    days_later = carry_day // 2
    if start_day:
        start_day = start_day.lower().capitalize()
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    if new_hour == 0:
        new_hour = 12

    new_period = "AM" if carry_day % 2 == 0 else "PM"

    new_time = f"{new_hour}:{str(new_minute).zfill(2)} {new_period}"

    if start_day:
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
