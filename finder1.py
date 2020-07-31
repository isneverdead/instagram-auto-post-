from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://platintakipci.com/member')
# loginbtn = browser.find_element_by_id("loginAsUser")
# browser.get('https://sicaktakipci.com/giris')
# userform = browser.find_element_by_id("username")
# passform = browser.find_element_by_name("password")
# userform.click()
# userform.sendKeys("taipulen")
userform.send_keys("taipulen")
userform.send_keys(Keys.TAB)
passform.send_keys("akbar123")
passform.send_keys(Keys.ENTER)
browser.get("https://platintakipci.com/tools/send-comment-like")
postform = browser.find_element_by_name("mediaUrl")
userpost = browser.find_element_by_name("username")
postform.click()
postform.send_keys("https://www.instagram.com/p/CA8NHDDHLAT/")
postform.send_keys(Keys.TAB)
userpost.send_keys("akbarpanel")
userpost.send_keys(Keys.ENTER)
numberlike = browser.find_element_by_name("adet")
numberlike.clear()
numberlike.send_keys("100")
comment = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[2]/form/div[2]/p").text
# /html/body/div[3]/div[2]/div[1]/div/div[2]/div[2]/p[1]
# /html/body/div[3]/div[2]/div[1]/div/div[2]/div[2]/p[2]