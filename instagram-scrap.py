# import autoit
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


mobile_emulation = {"deviceName": "Pixel 2"}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

username = "akbar_army_002"
password = "akbar021993"
image_path = "Dummy.jpg"
caption = "Hallo"
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.set_window_size(300, 860)
driver.get('https://instagram.com')


def login():
    login_button = driver.find_element_by_xpath(
        "//button[contains(text(),'Log In')]")
    login_button.click()
    sleep(3)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()


login()


sleep(4)


def close_reactivated():
    try:
        sleep(2)
        not_now_btn = driver.find_element_by_xpath(
            "//a[contains(text(),'Not Now')]")
        not_now_btn.click()
    except:
        pass


close_reactivated()


def close_notification():
    try:
        sleep(2)
        close_noti_btn = driver.find_element_by_xpath(
            "//button[contains(text(),'Not Now')]")
        close_noti_btn.click()
        sleep(2)
    except:
        pass


close_notification()


def close_add_to_home():
    sleep(3)
    close_addHome_btn = driver.find_element_by_xpath(
        "//button[contains(text(),'Cancel')]")
    close_addHome_btn.click()
    sleep(1)


close_add_to_home()

sleep(3)

close_notification()

new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
sleep(1.5)

# autoit.win_active("Open")
# sleep(2)
# autoit.control_send("Open", "Edit1", image_path)
# sleep(1.5)
# autoit.control_send("Open", "Edit1", "{ENTER}")

sleep(2)

next_btn = driver.find_element_by_xpath(
    "//button[contains(text(),'Next')]").click()

sleep(1.5)

caption_field = driver.find_element_by_xpath(
    "//textarea[@aria-label='Write a caption…']")
caption_field.send_keys(caption)

share_btn = driver.find_element_by_xpath(
    "//button[contains(text(),'Share')]").click()

sleep(25)

# user = driver.find_element_by_name('username')
# user.click()
# user.send_keys("akbar_army_002")
# passwo = driver.find_element_by_name('password')
# passwo.click()
# passwo.send_keys("akbar021993")
# passwo.send_keys(Keys.ENTER)
# driver.get('https://instagram.com')


# mobile_emulation = { "deviceName": "iphone X" }

# chrome_options = webdriver.ChromeOptions()

# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# driver = webdriver.Chrome(r'C:\Users\Alex\PythonDev\chromedriver')

# driver.get('https://www.google.com')
