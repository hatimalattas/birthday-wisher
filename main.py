##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import choice
import smtplib

# Today's date
now = dt.datetime.now()
month = now.month
day = now.day

# Sender Email information
my_email = "the.real.wealthy.academy@gmail.com"
password = "(1996)Ha"

# Reading the csv file and transform it into a dictionary
data = pandas.read_csv("./birthdays.csv")
birthdays = data.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv
for birthday in birthdays:
    if birthday["month"] == month and birthday["day"] == day:
        bd_name = birthday['name']
        bd_email = birthday["email"]

        # If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
        with open(f"./letter_templates/letter_{choice(range(1, 4))}.txt", "r") as letter:
            bd_msg = letter.read()
            bd_msg = bd_msg.replace("[NAME]", bd_name)
            print(bd_msg)

        # Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bd_email,
                msg=f"Subject:Happy Birthday {bd_name}!\n\n{bd_msg}"
            )
