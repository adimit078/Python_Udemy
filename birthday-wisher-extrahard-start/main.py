##################### Extra Hard Starting Project ######################
from pandas import read_csv
import datetime
import random
import smtplib

email = "toadityamittal@gmail.com"
password = "kmlv cmst ypnm xyfh"

# 1. Update the birthdays.csv
data = read_csv("birthdays.csv")
for (index,row) in data.iterrows():
    print(row.values)

# 2. Check if today matches a birthday in the birthdays.csv
curr_day = datetime.datetime.now().weekday()
curr_month = datetime.datetime.now().month

for (index,row) in data.iterrows():
    if (row.values[3] == curr_month and row.values[4] == curr_day):
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            message = (file.read().replace("[NAME]", row.values[0]))

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            
            connection.sendmail(from_addr=email, to_addrs=row.values[1], msg=f"Subject:Happy Birthday {row.values[0]} from Aditya\n\n{message}")





