'''
        -- deprecated --
check newDBCreation.ipynb for a better use
'''

import mysql.connector
import alumDB.database as DB
import csv


'''
Note that this code contains steps for alumDB update in 2018, some
steps may be unnecessary in future years.
'''
# access mysql
alumDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Yuhao123"
)

cursor = alumDB.cursor()

# insert into tables
# insert into person table
# with open("inserting_to_alumDB_18/newperson.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     names = list(reader)
#     # print(names)
# print((names[1]))
# for person in names[1:]:
#     print((person[0]))
#     sql = "INSERT INTO alumDB_18.person (pID, first_name, last_name, email, subject_field, degree, deg_start_month, deg_start_year, deg_end_month, deg_end_year, deg_received) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (int(person[0]), person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8], person[9], person[10])
#
#     cursor.execute(sql, val)
# cursor.execute("commit")

# # insert into linkedin_profile table
# with open("inserting_to_alumDB_18/linkedIn_profile.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     files = list(reader)
#     # print(names)
# for person in files[1:]:
#     print((person[0]))
#     sql = "INSERT INTO alumDB_18.linkedin_profile (pID, headline, location, summary, url, url_checked, url_added_manually, no_linkedin_known, url_changed, last_date_scraped) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (int(person[0]), person[1], person[2], person[3], person[4], person[5], person[6], person[7], person[8], person[9])
#
#     cursor.execute(sql, val)
# cursor.execute("commit")

# insert into education table
with open("inserting_to_alumDB_18/educations.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    edus = list(reader)
    print(edus[1])
for edu in edus[1:]:
    sql = "INSERT INTO alumDB_18.education (pID, dummy_index, school_name, subject_field, degree, deg_start_year, deg_end_year, deg_received, edu_source) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (edu[0], edu[1], edu[2], edu[3], edu[4], edu[5], edu[6], edu[7], edu[8])
    cursor.execute(sql, val)
cursor.execute("commit")

# # insert into experience table
# with open("inserting_to_alumDB_18/experiences.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     exps = list(reader)
#     print(exps[1])
# for exp in exps[1:]:
#     sql = "INSERT INTO alumDB_18.experience (pID, pos_title, company_name, pos_summary, pos_start_month, pos_start_year, pos_end_month, pos_end_year, location, exp_source) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (exp[0], exp[1], exp[2], exp[3], exp[4], exp[5], exp[6], exp[7], exp[8], exp[9])
#     cursor.execute(sql, val)
# cursor.execute("commit")

# # insert into skill table
# with open("inserting_to_alumDB_18/skills.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     skills = list(reader)
#     print(skills[1])
# for skill in skills[1:]:
#     sql = "INSERT INTO alumDB_18.skill (pID, skill_name, endorsement, skill_source) VALUES ( %s, %s, %s, %s)"
#     val = (skill[0], skill[1], skill[2], skill[3])
#     cursor.execute(sql, val)
# cursor.execute("commit")

# # create yearly database, e.g., alumDB_18
# DB.createDB(cursor, 'alumDB_18')
#
# # check databases
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)
#
# DB.useAlumDB(cursor, 'alumDB_18')
#
# # create tables
# DB.executeScriptsFromFile(cursor, "alumDB/PersonTable.sql")
# DB.executeScriptsFromFile(cursor, "alumDB/NameTable.sql")
# DB.executeScriptsFromFile(cursor, "alumDB/LinkedIn_profileTable.sql")
# DB.executeScriptsFromFile(cursor, "alumDB/ExperienceTable.sql")
# DB.executeScriptsFromFile(cursor, "alumDB/EducationTable.sql")
# DB.executeScriptsFromFile(cursor, "alumDB/SkillTable.sql")
# cursor.execute("commit")
#
# '''
# for 'person' and 'name table' we need to:
#       1. Copy old data from previous database
#       2. Add in new alumni data, this step can be ignored if there are no new alum.
# '''
# # Step 1
# # DB.copy_Table(cursor, "alumniTest.person", "alumDB_18.person")
# # DB.copy_Table(cursor, "alumniTest.name_table", "alumDB_18.name_table")
#
# # Step 2
#
#
# # to verify if one alum is already in the database
# # DB.assignPID(cursor, "new1.csv", "newAlum.csv", 588)
