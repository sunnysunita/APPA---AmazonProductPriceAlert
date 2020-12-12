import appa
from appa import APPA

url = "https://www.amazon.in/ASUS-UX481FL-BM5811T-Graphics-ScreenPad-Celestial/dp/B083BSFNYR/ref=redir_mobile_desktop?ie=UTF8&aaxitk=fmsAJwTuLR14w2NCHZXPKw&hsa_cr_id=7122201800402&pd_rd_r=fada79e4-e809-4af3-9975-92c393acdc48&pd_rd_w=frVlY&pd_rd_wg=UoF8C&ref_=sbx_be_s_sparkle_mcd_asin_0_img"
alert_price = 100000
email = "sunnysunita59@gmail.com"

laptop = APPA(url, alert_price, email)
print(laptop.run())