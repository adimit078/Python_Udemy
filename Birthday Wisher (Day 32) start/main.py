# import smtplib
#
# from pandas.core.methods.to_dict import to_dict
#
# email = "udemytest555@gmail.com"
# password = "hsff yxll vwjd cbjb"
#
# #Create Connection to gmail server
# with smtplib.SMTP("smtp.gmail.com") as connection:
#
#     #Secure using tls
#     connection.starttls()
#     #username and password
#     connection.login(user=email, password=password)
#
#     #Set up email and close
#     connection.sendmail(from_addr=email, to_addrs="toadityamittal@gmail.com",
#                         msg=""
#                             "Subject:Hello Drew Visconti @ Bolt Tower"
#                             "\n\nIf you are a handsome 5'Something italian-irish man with a goatee and a single in Bolt Tower - You have been selected - be prepared.")
#

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.weekday())
#
# date_of_birth = dt.datetime(month = 3, day = 18, year = 2005)

import random
import datetime as dt
import smtplib

curr_day = dt.datetime.now().weekday()

email = "udemytest555@gmail.com"
password = "hsff yxll vwjd cbjb"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)

    if (curr_day == 0):
        with open("quotes.txt") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]

            #DUMB WAY:
            # rand_message = lines[random.randint(0, len(lines))]
            rand_message = random.choice(lines)

        connection.sendmail(from_addr=email, to_addrs="toadityamittal@gmail.com",
                            msg = f"Subject:Your Monday Motivational Message\n\nHere is your daily motivational quote:\n{rand_message}")
        connection.sendmail(from_addr=email, to_addrs="acv49@cornell.edu",
                            msg=f"Subject:Your Monday Motivational Message\n\nHere is your daily motivational quote:\n{rand_message}")