import csv, time
from os import stat
from functions import Normalization

def parseHeader(person, driver):
    # top-card, for linkedIn_profile table
    # parse name
    try:
        person.name = driver.find_element_by_class_name(
            "pv-top-card-section__name").text.encode('utf-8').strip().decode()
    except Exception as e:
        person.name = ''
    print(person.name)
    # parse headline
    try:
        person.headline = driver.find_element_by_class_name("pv-top-card-section__headline").text.encode(
            'utf-8').strip().decode()
    except Exception as e:
        person.headline = ''

    # parse location
    try:
        person.location = driver.find_element_by_class_name("pv-top-card-section__location").text.encode(
            'utf-8').strip().decode()
        # print(person.location)
    except Exception as e:
        person.location = ''

    # parse summary
    # click the show more button if existed.
    try:
        button = driver.find_element_by_class_name("button.pv-top-card-section__summary-toggle-button")
        driver.execute_script("arguments[0].click();", button)
    except:
        pass

    try:
        person.summary = driver.find_element_by_class_name("pv-top-card-section__summary-text").text.encode(
            'utf-8').strip().decode()
    except Exception as e:
        person.summary = ''

    return driver

def saveHeader(linkedIn_profile):

    file = "resultCSV/linkedIn_profile.csv"

    if stat(file).st_size == 0:
        # file is empty
        writer_option = 'w'
    else:
        writer_option = 'a'

    with open(file, writer_option, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if writer_option == 'w':
            writer.writerow(('pid', 'headline', 'location', 'summary', 'url'))

        pID = []
        headline = []
        location = []
        summary = []
        url = []

        for item in linkedIn_profile:
            pID.append(item[0])
            headline.append(Normalization(item[1]))
            location.append(Normalization(item[2]))
            summary.append(Normalization(item[3]))
            url.append(Normalization(item[4]))

        writer.writerows(zip(pID, headline, location, summary, url))
