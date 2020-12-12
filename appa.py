import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys


class APPA():
    def __init__(self, product_URL, alert_price, email):
        """
        :param product_URL:
        :param alert_price:
        :param email:
        """
        self.__product_URL = product_URL
        self.__alert_price = alert_price
        self.__email = email
        self.__product_price = None
        self.__product_title = None
        self.__alert_client = False
        self.__price_difference = None

    def display(self):
        print("Product Title: ", self.__product_title)
        print("Product Price: ", self.__product_price)
        print("Alert Price: ", self.__alert_price)
        print("Price Difference: ", self.__price_difference)
        print("Alert Client: ", self.__alert_client)

    def getPrice(self):
        """
        scrap amazon website to get product_title and product_price
        store it in object instance variable
        product_title
        product_price
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
        response = requests.get(self.__product_URL, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.content, "html.parser")
        file = open("testproduct.html", "wb")
        file.write(soup.prettify("utf-8"))
        title = soup.find("span", attrs={"id": "productTitle", "class": "a-size-large"}).string.strip()
        self.__product_title = title
        temp = soup.find_all("a", attrs={"class": "a-accordion-row a-declarative accordion-header"})[1]
        price = temp.find("span", attrs={"class": "a-color-price"}).text.strip()
        lst = list(price)
        lst.remove(",")
        price = int(float("".join(lst)))
        self.__product_price = price
        #print(self.__product_price)

    def compare_price(self):
        """
        compare product_price and alert_price
        if product_price is less than the alert_price then set alert_client to True and store difference to price_difference
        else set alert_client to False
        :return:
        """
        if self.__product_price < self.__alert_price:
            #print("price drop...")
            self.__alert_client = True
            self.__price_difference = self.__product_price - self.__alert_price
        else:
            #print("Price not reduced...")
            self.__alert_client = False
            self.__price_difference = self.__product_price - self.__alert_price

    def send_email(self):
        """
        send the mail to the recipient using smtp protocol
        :return:
        """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sunnysunita.com@gmail.com", "tdcvgycwrzthjqgj")

        subject = "Price Fell Down"
        body = "Check the amazon link " + self.__product_URL
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            "sunnysunita.com@gmail.com",
            self.__email,
            message
        )
        #print("Our mail is sent!!!!")

    def run(self):
        """
        run all the important methods required for the APPA
        :return:
        """
        self.getPrice()
        #time.sleep(5)
        self.compare_price()
        #time.sleep(5)
        if self.__alert_client is True:
            self.send_email()
            #self.display()
            return True
        else:
            #self.display()
            return False


"""url = "https://www.amazon.in/ASUS-UX481FL-BM5811T-Graphics-ScreenPad-Celestial/dp/B083BSFNYR/ref=redir_mobile_desktop?ie=UTF8&aaxitk=fmsAJwTuLR14w2NCHZXPKw&hsa_cr_id=7122201800402&pd_rd_r=fada79e4-e809-4af3-9975-92c393acdc48&pd_rd_w=frVlY&pd_rd_wg=UoF8C&ref_=sbx_be_s_sparkle_mcd_asin_0_img"
alert_price = 100000
email_id = "sunnysunita59@gmail.com"
laptop = APPA(url, alert_price, email_id)
print(laptop.run())
"""