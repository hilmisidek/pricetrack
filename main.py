from pprint import pprint
import smtplib

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B00ALDPXE4/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
# Write your code below this line 👇

response = requests.get(URL, headers={"Accept-Language": "en-US,en;q=0.9,ms-MY;q=0.8,ms;q=0.7",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                    "(KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})

pricetrack = response.text

soup = BeautifulSoup(pricetrack, "html.parser")

pprint(soup)

title=soup.find(id="productTitle").getText().strip()
price=soup.find(name="span", class_="a-offscreen").getText().strip().split("$")
BUY_PRICE=200

fprice=float(price[1])

print (fprice)

if fprice<BUY_PRICE:
    message=f"{title} is now {fprice}"

    print (message)

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Price Alert"
    msg['From'] = "from address"
    msg['To'] = "to address"

    with smtplib.SMTP("mail server", port=587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        part1 = MIMEText(message, 'plain')
       # part2 = MIMEText("mailhtml", 'html')
        msg.attach(part1)
       # msg.attach(part2)
        result = connection.login("mail username", "mail password")
        connection.sendmail(msg['From'], msg['To'], msg.as_string())

        print (result)