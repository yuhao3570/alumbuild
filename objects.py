class Profile():
    pID = None
    name = None
    headline = None
    location = None
    summary = None

    def __init__(self, pID = None, name = None, headline = None, location = None, summary = None):
        self.pID = pID
        self.name = name
        self.headline = headline
        self.location = location
        self.summary = summary

    def __repr__(self):
        return "Name: {name} " \
               "Headline: {headline} " \
               "Location: {location} " \
               "Summary {summary}".format(
            name=self.name,
            headline=self.headline,
            location=self.location,
            summamry=self.summary)


class Education():
    pID = None
    school_name = None
    subject_field = None
    degree = None
    deg_duration = None

    def __init__(self, pID = None, school_name = None, subject_field = None, degree = None, deg_duration = None):
        self.pID = pID
        self.school_name = school_name
        self.subject_field = subject_field
        self.degree = degree
        self.deg_duration = deg_duration

    def __repr__(self):
        return "{degree} at {school_name} subject {subject_field} at {edu_duration} ".format(
            degree=self.degree,
            school_name=self.school_name,
            subject_field=self.subject_field,
            edu_duration=self.deg_duration)


class Experience():
    pID = None
    pos_title = None
    company_name = None
    pos_summary = None
    pos_duration = None
    location = None

    def __init__(self, pID = None, pos_title = None, company_name = None,
                 pos_summary = None, pos_duration = None, location = None):
        self.pID = pID
        self.pos_title = pos_title
        self.company_name = company_name
        self.pos_summary = pos_summary
        self.pos_duration = pos_duration
        self.location = location

    def __repr__(self):
        return "{pos_title} at {company_name} at {location} summary {pos_summary} duration {pos_duration}".format(
            pos_title=self.pos_title,
            company_name=self.company_name,
            location = self.location,
            pos_summary=self.pos_summary,
            pos_duration=self.pos_duration)


class Skill():
    pID = None
    skill_name = None
    endorsement = None

    def __init__(self, pID = None, skill_name=None, endorsement = '0'):
        self.pID = pID
        self.skill_name = skill_name
        self.endorsement = endorsement

    def __repr__(self):
        return "pId {pID} skill_name {skill_name} with {endorsement} endorement".format(
            pID = self.pID,
            skill_name=self.skill_name,
            endorsement = self.endorsement)


class Scraper(object):
    driver = None

    def is_signed_in(self):
        try:
            self.driver.find_element_by_id("profile-nav-item")
            return True
        except:
            pass
        return False

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element_by_class_name(class_name)
            return True
        except:
            pass
        return False
