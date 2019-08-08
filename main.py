#!/usr/bin/python2
# -*- coding:utf-8 -*-

import sys, getopt, csv, time
from selenium import webdriver
from person import Person
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from parser.linkedIn_profile import saveHeader
from parser.experience import saveExperiences, parseExpDuration
from parser.education import saveEducations, parseEduDuration
from parser.skill import saveSkills
import traceback


TIME_TO_SLEEP = 5
li_at = {'domain': '.www.linkedin.com',
         'expiry': 1596840285.423024,
         'httpOnly': True,
         'name': 'li_at',
         'path': '/',
         'secure': True,
         'value': 'AQEDAR54LTIDugIlAAABbHNn6GMAAAFsl3RsY00AdXkjtRfliwAD0CbXIieVE5L0WFc09e-py7gMYx9wzMVoMDDo9YMa0GdvGxuE4khTAPkrddvTc-yAAcPtQMGQ_0vW-tv8MQYll5xqi9fxJ0NeMHYr'}

linkedIn_profile = []
experiences = []
educations = []
skills = []

def pause(driver):
    print('Pause fetching for ' + str(TIME_TO_SLEEP) + ' seconds')
    try:
        driver.get('http://www.google.com/')
        element = WebDriverWait(driver, 10).until(EC.title_contains('Google'))
    finally:
        time.sleep(TIME_TO_SLEEP * 6)  # 6 times the standard time.

def processProfile(driver, data, index, pause_cnt):
    if pause_cnt and index % pause_cnt == 0:
        pause(driver)
    log = open("log.txt", "w")
    try:
        print('Processing profile ' + str(index) + ' ... ' + str(data[1]))
        profile = Person(pID=str(data[0]), linkedIn_url=data[1], driver=driver)
        print(profile.linkedIn_url)
        profile.experiences = []  # Needed due to a bug in the library
        profile.educations = []  # Needed due to a bug in the library
        profile.skills = []
        # print("pid is: ", profile.pID)

        # scraping starts here
        profile.scrape(close_on_complete=False)
        # print("scraping done!")
        # storing details here, followed the same order as respective tables in database

        # add a check if one profile has neither experience, education or skill
        if profile.hasSkill + profile.hasEdu + profile.hasExp == 0:
            raise ValueError("Nothing found in the profile")

        # storing header
        linkedIn_profile.append([profile.pID, profile.headline, profile.location, profile.summary, profile.linkedIn_url])

        # print("profile done!")
        # storing experiences
        if profile.hasExp:
            for exp in profile.experiences:
                # divide duration
                pos_start_month, pos_start_year, pos_end_month, pos_end_year = parseExpDuration(exp.pos_duration)

                experiences.append([
                    exp.pID, exp.pos_title, exp.company_name, exp.pos_summary, pos_start_month,
                    pos_start_year, pos_end_month, pos_end_year, exp.location
                ])
            # print("exp storing done!")

        # store educations
        if profile.hasEdu:
            for edu in profile.educations:
                # deg_start_year, deg_end_year = parseEduDuration(edu.edu_duration)
                educations.append(
                    [edu.pID, edu.school_name, edu.subject_field, edu.degree, edu.deg_duration])
            # print("edu storing done!")

        # store skills
        if profile.hasSkill:
            for sk in profile.skills:
                skills.append([sk.pID, sk.skill_name, sk.endorsement])

    except:
        e = sys.exc_info()[0]
        print('Error processing ' + str(data[1]) + ' error: ' + str(e))
        with open("failed.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([str(data[0]), data[1], str(e)])
        log.writelines(str('[%s] error= %s ' % (profile.name, str(e))))
        pass
    traceback.print_exc()
    return len(linkedIn_profile)


def getDriver(headless):

    options = Options()
    if headless:
        options.add_argument('headless')

    options.add_argument("--normal")
    # options.add_argument("--start-maximized")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--auto-open-devtools-for-tabs")
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(chrome_options=options)

    # need to first go to the website to add cookie
    driver.get('http://www.linkedin.com/')
    try:
        driver.add_cookie(li_at)
    except:
        print('Error loading cookie!')
        sys.exit()
    return driver


def main(argv):
    usage = 'main.py -i <inputfile>  [-j] [-n <count>] [-s <startpoint>] [-e <endpoint>]'
    headless = False
    pause_cnt = 0
    start = 0
    end = 1000

    try:
        # import pdb;pdb.set_trace()
        opts, args = getopt.getopt(argv, "jn:i:s:e:")
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-i':
            inputfile = arg
        elif opt == '-j':
            # Chrome will be in headless mode
            headless = True
        elif opt == '-n':
            # Add a pause every <count> profiles to avoid throttling by Linkedin
            pause_cnt = int(arg)
        elif opt =='-s':
            start = int(arg)
        elif opt =='-e':
            end = int(arg)

    driver = getDriver(headless)

    # Process input
    with open(inputfile) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        profiles = list(reader)

    profile_num = len(profiles)
    print('Processing ' + str(profile_num) + ' profiles')
    for index, row in enumerate(profiles):
        cur = int(row[0])
        if start <= cur <= end:
            if row[1] == "NULL":
                print("No url for ", row[0])
                continue
            size= processProfile(driver, row, index+1, pause_cnt)
            time.sleep(TIME_TO_SLEEP)  # Always sleep a bit between one profile and another.
            print(str(size))


    # Create output
    # save to linkedIn_profile.csv
    saveHeader(linkedIn_profile)

    # save to experiences.csv
    saveExperiences(experiences)

    # save to ecucations.csv
    saveEducations(educations)

    # save to skills.csv
    saveSkills(skills)


if __name__ == "__main__":
    main(sys.argv[1:])
