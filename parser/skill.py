from objects import Skill
from functions import Normalization
from os import stat
import csv, time
import traceback

def parseSkill(person, driver):

    ski = driver.find_element_by_class_name("pv-skill-categories-section")

    # expand all skills
    try:
        button = ski.find_element_by_class_name("pv-skills-section__additional-skills")
        driver.execute_script("arguments[0].click();", button)

        time.sleep(3)
        ski = driver.find_element_by_class_name("pv-skill-categories-section")
    except:
        pass

    for sk in ski.find_elements_by_class_name(
            "pv-skill-category-entity__skill-wrapper"):
        # parse skills
        try:
            skill_name = sk.find_element_by_class_name(
                "pv-skill-category-entity__name-text").text.encode(
                'utf-8').strip().decode()
        except Exception as e:
            skill_name = ''
        # print(skill_name)

        # parse endorsement
        try:
            endorsement = sk.find_element_by_class_name(
                "pv-skill-category-entity__endorsement-count").text.encode(
                'utf-8').strip().decode()
        except Exception as e:
            endorsement = '0'
        # print("endorsement: ", endorsement)

        person.add_skill(
            Skill(pID=person.pID,
                  skill_name=skill_name,
                  endorsement=endorsement)
        )
    return driver

def saveSkills(skills):
    file = "resultCSV/skills.csv"
    if stat(file).st_size == 0:
        # file is empty
        writer_option = 'w'
    else:
        writer_option = 'a'

    with open(file, writer_option, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if writer_option == 'w':
            writer.writerow(('pid', 'skill_name', 'endorsement'))
        pID = []
        skill_name = []
        endorsement = []
        for item in skills:
            pID.append(item[0])
            skill_name.append(Normalization(item[1]))
            endorsement.append(item[2])
        writer.writerows(zip(pID, skill_name, endorsement))