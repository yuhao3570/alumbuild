from selenium import webdriver

from parser.linkedIn_profile import parseHeader
from parser.experience import parseExperience
from parser.education import parseEdu
from parser.skill import parseSkill
from functions import scroll, clickButtons

import os

class Person():
    pID = None
    name = None
    headline = None
    location = None
    summary = None
    linkedIn_url = None

    # this to keep track where there are such section in profile
    hasExp = False
    hasEdu = False
    hasSkill = False

    experiences = []
    educations = []
    skills = []

    def __init__(self, name = None, pID = None, headline = None, location = None, summary = None, linkedIn_url=None,
                 hasExp=False, hasEdu = False, hasSkill = False, experiences=[], educations=[], skills=[], driver=None, get=True):
        self.pID = pID
        self.name = name
        self.headline = headline
        self.location = location
        self.summary = summary
        self.linkedIn_url = linkedIn_url
        self.hasExp = hasExp
        self.hasEdu = hasEdu
        self.hasSkill = hasSkill
        self.experiences = experiences
        self.educations = educations
        self.skills = skills

        if driver is None:
            try:
                if os.getenv("CHROMEDRIVER") == None:
                    driver_path = os.path.join(
                        os.path.dirname(__file__), 'drivers/chromedriver')
                else:
                    driver_path = os.getenv("CHROMEDRIVER")

                driver = webdriver.Chrome(driver_path)
            except:
                driver = webdriver.Chrome()

        if get:
            driver.get(linkedIn_url)

        self.driver = driver

    def add_experience(self, experience):
        self.experiences.append(experience)

    def add_education(self, education):
        self.educations.append(education)

    def add_skill(self, skill):
        self.skills.append(skill)

    def scrape(self, close_on_complete=True):
        self.scrape_logged_in(close_on_complete=close_on_complete)

    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        # print("start scraping!")

        # to expand all 'show more' buttons in experience and education sections
        scroll(driver)
        # clickButtons(driver, "pv-profile-section__see-more-inline")

        scroll(driver)
        print("here")

        # parse header
        parseHeader(self, driver)
        print("parsing header done!")

        # parse experiences
        try:
            driver.find_element_by_id("experience-section")
            self.hasExp = True
            parseExperience(self, driver)
            print("experience Done!")
        except Exception as e:
            print("no Exp section exist!")
            pass

        # parse educations
        try:
            driver.find_element_by_id("education-section")
            self.hasEdu = True
            parseEdu(self, driver)
            print("education Done!")
        except Exception as e:
            print("no Edu section exist!")
            pass

        # parse skills
        try:
            driver.find_element_by_class_name("pv-skill-categories-section")
            self.hasSkill = True
            parseSkill(self, driver)
            print("skill done!")
        except Exception as e:
            print("no skill section exist!")
            pass

        # save page source
        out_path = '/Users/hao/PycharmProjects/alumBuild/html/'
        if not os.path.exists(out_path):
            os.makedirs(out_path)

        pagesource = open(out_path + str(self.name) + '.html', 'w')
        pagesource.write(str(driver.page_source.encode('utf-8')))
        pagesource.close()
        print("Save Page Source to %s " % (self.name))
        if close_on_complete:
            driver.close()
        # print("scraping done")

    # def scrape_not_logged_in(self, close_on_complete=True, retry_limit=10):
    #     driver = self.driver
    #     retry_times = 0
    #     while self.is_signed_in() and retry_times <= retry_limit:
    #         page = driver.get(self.linkedin_url)
    #         retry_times = retry_times + 1
    #
    #     # get name
    #     self.name = driver.find_element_by_id("name").text.encode(
    #         'utf-8').strip()
    #
    #     # get experience
    #     exp = driver.find_element_by_id("experience")
    #     for position in exp.find_elements_by_class_name("position"):
    #         position_title = position.find_element_by_class_name(
    #             "item-title").text.encode('utf-8').strip()
    #         company = position.find_element_by_class_name(
    #             "item-subtitle").text.encode('utf-8').strip()
    #
    #         times = position.find_element_by_class_name(
    #             "date-range").text.encode('utf-8').strip()
    #         experience = Experience(position_title=position_title, times=times)
    #         experience.institution_name = company
    #         self.add_experience(experience)
    #
    #     # get education
    #     edu = driver.find_element_by_id("education")
    #     for school in edu.find_elements_by_class_name("school"):
    #         university = school.find_element_by_class_name(
    #             "item-title").text.encode('utf-8').strip()
    #         degree = school.find_element_by_class_name("original").text.encode(
    #             'utf-8').strip()
    #
    #         times = school.find_element_by_class_name(
    #             "date-range").text.encode('utf-8').strip()
    #
    #         education = Education(times=times, degree=degree)
    #         education.institution_name = university
    #         self.add_education(education)
    #
    #     # get
    #     if close_on_complete:
    #         driver.close()

    def __repr__(self):
        return "{name}\n{headline}\n{location}\n{summary}\nHasExp:{hasExp}\nHasEdu:{hasEdu}\nHasSkill:{hasSkill}\n\nExperience\n{exp}\n\nEducation\n{edu}\n\nSkill\n{ski}".format(
            name=self.name,
            headline=self.headline,
            location=self.location,
            summary=self.summary,
            hasExp=self.hasExp,
            hasEdu=self.hasEdu,
            hasSkill=self.hasSkill,
            exp=self.experiences,
            edu=self.educations,
            ski=self.skills)