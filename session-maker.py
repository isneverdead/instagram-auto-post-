# import autoit
# import pyautogui
import pickle
import pprint
import keyboard
from logininfo import login_info
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# (x=300, y=388)
# double click (x=658, y=194)

PROXY = "34.101.253.132:3128"  # akbar_army_002
# PROXY = "34.101.173.97:3128"  # akbar_army_004
# PROXY = "34.101.231.97:3128"  # akbar_army_005
# PROXY = "34.101.116.128:3128"  # akbar_army_006
# PROXY = "34.87.145.222:3128"  # akbar_army_007

mobile_emulation = {"deviceName": "Pixel 2"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

username = login_info.username_data
password = login_info.password_data
image_path = "Dummy.jpg"
caption = "Hallo"


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):  # Checks if the instance expiry a float
            # it converts expiry cookie to a int
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "/opt/lampp/htdocs/SMM Project/python-elemen-finder/" + \
    str(username)+".txt"

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.set_window_size(300, 860)

driver.get('https://google.com')


def login():
    login_button = driver.find_element_by_xpath(
        "//button[contains(text(),'Log In')]")
    login_button.click()
    sleep(1.2)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(password)
    password_input.submit()


def check_login():
    try:
        driver.get('https://instagram.com/')
        login()
        sleep(2)
        save_cookies(driver, cookies_location)
    except:
        # load_cookies(driver, cookies_location)
        pass

        # login()
        # driver.get('https://instagram.com/')

        # check_login()
        # cookies = driver.get_cookies()
        # print(cookies)
        # sleep(2)
        # driver.get('https://instagram.com/')

        # sleep(2.5)


def close_reactivated():

    try:
        sleep(2)
        not_now_btn = driver.find_element_by_xpath(
            "//a[contains(text(),'Not Now')]")
        not_now_btn.click()
    except:
        pass


# close_reactivated()


def close_notification():
    try:
        sleep(2)
        close_noti_btn = driver.find_element_by_xpath(
            "//button[contains(text(),'Not Now')]")
        close_noti_btn.click()
        sleep(2)
    except:
        pass


# close_notification()


def close_add_to_home():
    sleep(3)
    close_addHome_btn = driver.find_element_by_xpath(
        "//button[contains(text(),'Cancel')]")
    close_addHome_btn.click()
    sleep(1)


# close_add_to_home()

# sleep(3)

# close_notification()


def post_image():
    new_post_btn = driver.find_element_by_xpath(
        "//div[@role='menuitem']").click()
    # tombol = driver.find_element_by_xpath("//*[@aria-label='New Post']")
    sleep(1.5)
    # pyautogui
    # pyautogui.moveTo(300, 388)
    # pyautogui.click()
    # sleep(1)
    # pyautogui.moveTo(658, 194)
    # pyautogui.doubleClick()
    # sleep(2)
    # autoit
    # autoit.win_active("Open")
    # sleep(2)
    # autoit.control_send("Open", "Edit1", image_path)
    # sleep(1.5)
    # autoit.control_send("Open", "Edit1", "{ENTER}")
    keyboard.send("tab")
    keyboard.send("tab")
    keyboard.send("tab")
    keyboard.send("end")
    keyboard.send("tab")
    keyboard.send("tab")
    keyboard.send("tab")
    sleep(0.1)
    keyboard.send("end")
    sleep(0.1)
    keyboard.send("enter")
    sleep(4)
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
