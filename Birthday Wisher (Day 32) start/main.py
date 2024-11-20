import smtplib

from pandas.core.methods.to_dict import to_dict

email = "udemytest555@gmail.com"
password = "hsff yxll vwjd cbjb"

#Create Connection to gmail server
with smtplib.SMTP("smtp.gmail.com") as connection:

    #Secure using tls
    connection.starttls()
    #username and password
    connection.login(user=email, password=password)

    #Set up email and close
    connection.sendmail(from_addr=email, to_addrs="acv49@cornell.edu",
                        msg=""
                            "Subject:Hello Drew Visconti @ Bolt Tower"
                            "\n\nIf you are a handsome 5'Something italian-irish man with a goatee and a single in Bolt Tower - You have been selected - be prepared.")

