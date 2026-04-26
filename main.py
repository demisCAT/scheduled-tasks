# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas
import datetime as dt
import random as rd
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL=os.environ.get("MY_EMAIL")
MY_PASSWORD=os.environ.get("MY_PASSWORD")


now = dt.datetime.now()
today = (now.month, now.day)

birth_data = pandas.read_csv("birthdays.csv")

birthdays_dict = {  (row_data["month"], row_data["day"]):row_data
                    for (index,row_data)
                    in birth_data.iterrows()
                 }

if today in birthdays_dict:
    # print(today)
    birthday = birthdays_dict[today]

    with (open(f"./Letter_templates/letter_{rd.randint(1,3)}.txt", mode="r") as letter):
        letter_txt = str(letter.read())
        birth_name = birthday["name"]
        replace_text = letter_txt.replace("[NAME]", birth_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs="jbarrosoq@protonmail.com",
                            msg=f"Subject:Happy Birthday!!\n\n{replace_text}",
                            )
        connection.close()
