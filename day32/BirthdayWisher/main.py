import os
import pandas
import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
load_dotenv()
PLACEHOLDER = "[NAME]"
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("day32/BirthdayWisher/birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(
        file=f"day32/BirthdayWisher/letter_templates/letter_{random.randint(1, 3)}.txt"
    ) as letter:
        content = letter.read()
        content = content.replace(PLACEHOLDER, birthday_person["name"])
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=os.environ["my_email"], password=os.environ["password"])
        connection.sendmail(
            from_addr=os.environ["my_email"],
            to_addrs=f"{birthday_person["email"]}",
            msg=f"Subject  : Happy Birthdy {content}",
        )
        
        
