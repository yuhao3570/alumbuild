from objects import Experience
from functions import Normalization
from os import stat
import csv, traceback
from functions import monToNum, clickButtons

def parseExperience(person, driver):

    exp = driver.find_element_by_id("experience-section")

    try:
        exp = clickButtons(driver, exp, "experience-section", "pv-profile-section__see-more-inline")
    except:
        pass

    # loop through every positions
    for position in exp.find_elements_by_class_name("pv-position-entity"):
        # verify if there are multiple positions in this experience
        groups = 0

        try:
            groups = position.find_element_by_class_name("pv-entity__role-details")
        except Exception as e:
            # traceback.print_exc()
            pass

        if groups == 0:
            parseSingleExp(person, position)  # in this case, there is only one title per experience
        else:
            parseMultiExp(person, position)
    return driver

# this function handles the case when there is only one title in one company/experience
def parseSingleExp(person, position):
    # parse title
    try:
        pos_title = position.find_element_by_tag_name(
            "h3").text.encode('utf-8').strip().decode()
    except Exception as e:
        # traceback.print_exc()
        pos_title = ''

    # parse company_name
    try:
        company_name = position.find_element_by_class_name(
            "pv-entity__secondary-title").text.encode('utf-8').strip().decode()
    except Exception as e:
        # traceback.print_exc()
        company_name = ''
    print("company name: ", company_name)
    # parse location
    try:
        location = position.find_element_by_class_name("pv-entity__location").find_elements_by_tag_name(
            'span')[1].text.encode('utf-8').strip().decode()
    except Exception as e:
        # traceback.print_exc()
        location = ''

    # parse pos_duration
    try:
        pos_duration = position.find_element_by_class_name("pv-entity__date-range").find_elements_by_tag_name(
            'span')[1].text.encode('utf-8').strip().decode()
    except Exception as e:
        # traceback.print_exc()
        pos_duration = ''

    # parse pos_summary
    try:
        pos_summary = position.find_element_by_class_name("pv-entity__description").text.encode(
                                        'utf-8').strip().decode()
    except Exception as e:
        # traceback.print_exc()
        pos_summary = ''

    experience = Experience(pID = person.pID, company_name = company_name,
                            pos_title = pos_title, pos_summary = pos_summary,
                            pos_duration = pos_duration, location = location)
    person.add_experience(
        experience
        # Experience(person.pID, company_name, pos_title, pos_summary, pos_duration, location)
    )

# this function handles the case when there are multiple titles in one company/experience
def parseMultiExp(person, position):
    # in this case, company will be at the top, followed by several blocks of experiences
    # print("parse multiple")
    try:
        company_name= position.find_element_by_class_name(
            "pv-entity__company-summary-info").find_element_by_tag_name(
            "h3").find_elements_by_tag_name("span")[1].text.encode('utf-8').strip().decode()
    except Exception as e:
        traceback.print_exc()
        company_name = ''
    # print("c: ", company_name)

    groups = position.find_elements_by_class_name("pv-entity__role-details")
    for group in groups:
        # parse title
        try:
            pos_title = group.find_element_by_tag_name("h3").find_elements_by_tag_name(
                "span")[1].text.encode('utf-8').strip().decode()
        except Exception as e:
            # traceback.print_exc()
            pos_title = ''

        # parse location
        try:
            location = group.find_element_by_class_name("pv-entity__location").find_elements_by_tag_name(
                'span')[1].text.encode('utf-8').strip().decode()
        except Exception as e:
            # traceback.print_exc()
            location = ''

        # parse pos_duration
        try:
            pos_duration = group.find_element_by_class_name("pv-entity__date-range").find_elements_by_tag_name(
                'span')[1].text.encode('utf-8').strip().decode()
        except Exception as e:
            pos_duration = ''
            # traceback.print_exc()


        # parse pos_summary
        try:
            pos_summary = group.find_element_by_class_name("pv-entity__description").text.encode(
                'utf-8').strip().decode()
        except Exception as e:
            pos_summary = ''
            # traceback.print_exc()

        experience = Experience(pID=person.pID,
                       company_name=company_name,
                       pos_title=pos_title,
                       pos_summary=pos_summary,
                       pos_duration=pos_duration,
                       location=location)
        person.add_experience(
            experience
        )

def saveExperiences(experiences):
    file = "resultCSV/experiences.csv"

    if stat(file).st_size == 0:
        # file is empty
        writer_option = 'w'
    else:
        writer_option = 'a'

    with open(file, writer_option, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if writer_option == 'w':
            writer.writerow(('pid', 'pos_title', 'company_name',  'pos_summary', 'pos_start_month',
                             'pos_start_year', 'pos_end_month', 'pos_end_year', 'location'))

        pID = []
        pos_title = []
        company_name = []
        pos_summary = []
        pos_start_month = []
        pos_start_year = []
        pos_end_month = []
        pos_end_year = []
        location = []

        for item in experiences:
            pID.append(item[0])
            pos_title.append(Normalization(item[1]))
            company_name.append(Normalization(item[2]))
            pos_summary.append(Normalization(item[3]))
            pos_start_month.append(Normalization(item[4]))
            pos_start_year.append(Normalization(item[5]))
            pos_end_month.append(Normalization(item[6]))
            pos_end_year.append(Normalization(item[7]))
            location.append(Normalization(item[8]))

        writer.writerows(
            zip( pID, pos_title, company_name, pos_summary, pos_start_month,
                             pos_start_year, pos_end_month, pos_end_year, location))


def parseExpDuration(times):
    startMon = '00'
    startYear = '0000'
    endMon = '00'
    endYear = '0000'

    time = times.split("–")

    if len(time) > 1:
        if len(time[0].strip()) == 4:
            startYear = time[0].strip()
        else:
            start = time[0].strip().split(" ")
            startMon = monToNum(start[0].strip())
            startYear = start[1]

        p = time[1].find("Present")

        if p == -1:
            if len(time[1].strip()) == 4:
                endYear = time[1].strip()
            else:
                end = time[1].strip().split(" ")
                endMon = monToNum(end[0].strip())
                endYear = end[1]

        else:
            endMon = '13'
            endYear = '9999'
    return startMon, startYear, endMon, endYear