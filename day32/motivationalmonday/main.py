import os
import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
load_dotenv()
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # -----------------Getting a random quote from file--------------------#
    with open(file="day32/motivationalmonday/quotes.txt") as Quotefile:
        global RANDOM_QUOTE
        Quote_list = Quotefile.readlines()
        RANDOM_QUOTE = random.choice(Quote_list)
        # print(RANDOM_QUOTE)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=os.environ["my_email"], password=os.environ["password"])
    connection.sendmail(
        from_addr=os.environ["my_email"],
        to_addrs="ajaykh053@gmail.com",
        msg=f"Subject : Hello\n\nGood Morning\n\nMonday's Motivational Quote : \n\n{RANDOM_QUOTE}",
    )
#     connection.close()
