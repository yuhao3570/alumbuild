# this code to store parsed output into respective CSVs

import csv, os

def saveHeader (linkedIn_profile):
    with open("resultCSV/linkedIn_profile.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        csvfile.seek(0)  # ensure you're at the start of the file..
        first_char = csvfile.read(1)  # get the first character

        if not first_char:
            # file is empty, write header in
            writer.writerow(('pid', 'name', 'headline', 'location', 'summary'))
        else:
            csvfile.seek(0)
            writer.writerow(('pid', 'name', 'headline', 'location', 'summary'))
            pID = []
            name = []
            headline = []
            location = []
            summary = []

        for item in linkedIn_profile:
            pID.append(item[0])
            name.append(item[1])
            headline.append(item[2])
            location.append(item[3])
            summary.append(item[4])
        writer.writerows(zip(pID, name, headline, location, summary))

def saveEdu(educations):
    with open("resultCSV/educations.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('pID', 'School_name', 'degree', 'Subject_fireld', 'times'))
        pID = []
        school_name = []
        degree = []
        subject_field = []
        duration = []
        for item in educations:
            pID.append(Normalization(item[0]))
            school_name.append(Normalization(item[1]))
            degree.append(Normalization(item[2]))
            subject_field.append(Normalization(item[3]))
            duration.append(Normalization(item[4]))
        writer.writerows(zip(pID, school_name, degree, subject_field, duration))

def saveExp(experiences):
    with open("resultCSV/experiences.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('pID', 'pos_title', 'company_name',
                         'pos_summary', 'startMon', 'startYear', 'endMon', 'endYear', 'location'))
        pID = []
        company_name = []
        pos_title = []
        pos_summary = []
        startMon = []
        startYear = []
        endMon = []
        endYear = []
        location = []
        for item in experiences:
            pID.append(Normalization(item[0]))
            pos_title.append(Normalization(item[1]))
            company_name.append(Normalization(item[2]))
            pos_summary.append(Normalization(item[3]))
            startMon.append(Normalization(item[4]))
            startYear.append(Normalization(item[5]))
            endMon.append(Normalization(item[6]))
            endYear.append(Normalization(item[7]))
            location.append(Normalization(item[8]))
        writer.writerows(
            zip(pID, company_name, pos_title, pos_summary, startMon, startYear, endMon, endYear, location))

def saveSkills(skills):
    with open("resultCSV/skills.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('pID', 'Skill_name'))
        pID = []
        skill_name = []
        for item in skills:
            pID.append(Normalization(item[0]))
            skill_name.append(Normalization(item[1]))
        writer.writerows(zip(pID, skill_name))

def Normalization(value):
    return value if not (value is None) else ''