from objects import Education
from functions import Normalization, clickButtons
from os import stat
import csv

def parseEdu(person, driver):

    # get all educations
    edu = driver.find_element_by_id("education-section")

    try:
        edu = clickButtons(driver, edu, "education-section", "pv-profile-section__see-more-inline")
    except:
        pass

    for school in edu.find_elements_by_class_name("pv-profile-section__sortable-item"):
        # parse school_name
        try:
            school_name = school.find_element_by_class_name(
                "pv-entity__school-name").text.encode('utf-8').strip().decode()
                # print("\nschool", school_name)
        except Exception as e:
            school_name = ''

        # parse degree
        try:
            degree = school.find_element_by_class_name("pv-entity__degree-name").find_elements_by_tag_name(
                    'span')[1].text.encode('utf-8').strip().decode()

        except Exception as e:
            degree = ''
        # print("degree", degree)

        # parse subject_field
        try:
            subject_field = school.find_element_by_class_name("pv-entity__fos").find_elements_by_tag_name(
                    'span')[1].text.encode('utf-8').strip().decode()

        except Exception as e:
            subject_field = ''
        # print("subject:", subject_field)

        # parse duration
        try:
            edu_duration = school.find_element_by_class_name("pv-entity__dates").find_elements_by_tag_name(
                    'span')[1].text.encode('utf-8').strip().decode()
        except Exception as e:
            edu_duration = ''
            # print("duration", edu_duration)

        person.add_education(
                Education(person.pID, school_name, degree, subject_field, edu_duration))

def saveEducations(educations):
    file = "resultCSV/educations.csv"

    if stat(file).st_size == 0:
        # file is empty
        writer_option = 'w'
    else:
        writer_option = 'a'

    with open(file, writer_option, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if writer_option == 'w':
            # writer.writerow(('pid', 'school_name', 'subject_field', 'degree', 'deg_start_year', 'deg_end_year'))
            writer.writerow(('pid', 'school_name', 'subject_field', 'degree', 'deg_duration'))

        pID = []
        school_name = []
        subject_field = []
        degree = []
        deg_duration = []
        # deg_start_year = []
        # deg_end_year = []

        for item in educations:
            pID.append(Normalization(item[0]))
            school_name.append(Normalization(item[1]))
            subject_field.append(Normalization(item[2]))
            degree.append(Normalization(item[3]))
            deg_duration.append(Normalization(item[4]))

            # deg_start_year.append(Normalization(item[4]))
            # deg_end_year.append(Normalization(item[5]))

        writer.writerows(zip(pID, school_name, subject_field, degree, deg_duration))


def parseEduDuration(times):
    deg_start_year = '0000'
    deg_end_year = '0000'

    time = times.split("–")

    length = len(time)
    if length == 1:
        deg_start_year = time[0].strip()
    if length == 2:
        deg_start_year = time[0].strip()
        deg_end_year = time[1].strip()

    return deg_start_year, deg_end_year

# print(parseEduDuration("1995 - 1997"))