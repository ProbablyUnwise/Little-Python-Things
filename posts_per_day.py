import datetime

register_date = datetime.date(2011, 12, 3)
todays_date = datetime.date.today()
days_old = (todays_date-register_date).days
posts_per_day = round(days_old/365)
print("You need to make " + str(posts_per_day) + " posts every day")
print("to catch up in one year, or " + str(posts_per_day*2))
print("posts per day to do it six months. Happy posting!")
