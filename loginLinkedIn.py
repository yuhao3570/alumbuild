# This code to login to LinkedIn and store the cookie information
# LinkedIn Cookie for user named as "li_at"
# need to run in terminal:
#   python loginLinkedIn.py -u linkedIn_username -p passward [-j]
# Copy the printed cookie result and assign it to li_at variable in main.py
# Author: Hao

import sys, getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def login(user, password, headless):
    """
    This function to login to LinkedIn
    :param user: LinkedIn username
    :param password: password
    :param headless: T/F to indicate use of headless or not
    :return: return a driver with LinkedIn cookie
    """
    print('Logging into Linkedin...')
    # options = webdriver.ChromeOptions()
    options = Options()
    if headless:
        options.add_argument('headless')

    options.add_argument("--normal")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username')))
        element = driver.find_element_by_name('session_key')
        element.send_keys(user)
        print(user)
        element = driver.find_element_by_name('session_password')
        element.send_keys(password, Keys.ENTER)
    except:
        print('Error logging into Linkedin')
        sys.exit(2)

    while True:
        a = input("Login Complete input 1:")
        if a == '1':
            break
    return driver

def main(argv):
    """
    To obtain LinkedIn User cookie: li-at
    need to run through terminal
    python loginLinkedIn.py -u username -p password [-j]
    :param argv:
    :return:
    """
    usage = 'loginLinkedIn.py -u <user> -p <password> [-j] [-n <count>]'
    headless = False
    try:
        # import pdb;pdb.set_trace()
        opts, args = getopt.getopt(argv, "jn:u:p:")
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-u':
            # for username
            user = arg
        elif opt == '-p':
            # for password
            password = arg
        elif opt == '-j':
            # Chrome will be in headless mode
            headless = True
        elif opt == '-n':
            # Add a pause every <count> profiles to avoid throttling by Linkedin
            pause_cnt = int(arg)
    driver = login(user, password, headless)
    li_at = driver.get_cookie("li_at")
    print(li_at)
    driver.quit()

if __name__ == "__main__":
    main(sys.argv[1:])