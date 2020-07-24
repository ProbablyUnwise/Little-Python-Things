# Take the date you registered on a forum and counts how many
# posts per day you would have to make to cath up
import datetime

register_date = datetime.date(2011, 12, 3)
todays_date = datetime.date.today()
days_old = (todays_date-register_date).days

current_posts = 260
needed_posts = days_old-current_posts
posts_per_day = round(needed_posts/365)

out_msg = (
    f"You need to make {posts_per_day} posts every day to\n"
    f"catch up in one year, or {posts_per_day*2} posts\n"
    f"per day to do it six months."
)

print(out_msg)
