# -*- coding:utf-8 -*-
import re, time, traceback

def monToNum(month):
    if month == "Jan":
        return "01"
    elif month == "Feb":
        return "02"
    elif month == "Mar":
        return "03"
    elif month == "Apr":
        return "04"
    elif month == "May":
        return "05"
    elif month == "Jun":
        return "06"
    elif month == "Jul":
        return "07"
    elif month == "Aug":
        return "08"
    elif month == "Sep":
        return "09"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    else:
        return "12"


def Normalization(value):
    return value if not (value is None) else ''


def scroll(driver):
    '''
    this function to scroll up and done the window to ensure the page is fully loaded.
    :param driver:
    '''
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/4));")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, Math.ceil(-document.body.scrollHeight*6/7));")
    time.sleep(1)


def clickButtons(driver, sec, secStr,  buttonstr):
    '''
    this function to recursively find and click all 'view more' buttons
    :param driver:
    '''
    try:
        button = sec.find_element_by_class_name(buttonstr)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        sec = driver.find_element_by_id(secStr)

        sec = clickButtons(driver, sec, secStr, buttonstr)
    except Exception as e:
        # traceback.print_exc()
        return sec
    return sec


