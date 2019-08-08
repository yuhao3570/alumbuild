# alumbuild
This project reads in alumni names and search fro their LinkedIn profile. Then scrape and parse profiles and saves as a MySQL database.

## requirements
1. chromedriver
2. selenium
3. mysql.connector

## Run searchNewLinks 
This step to obtain possible profile links of each alumni. Manual validation needed tp select the one ture profile.

## Run loginLinkedIn.py 
```python
python loginLinkedIn.py -u username -p password
```
This to obtain linkedIn unser cookie. This project scrapes linkedIn at login. No fake proxy ip is used.
LinkedIn recently started to randomly ask for robot check at login, this project would not bypass it at headless mode. i.e., use non-headless mode and pass the robot check manually.

## Run main.py with updated cookie info
```python
python main.py -i testLinks.csv -j
```
This step will run through all profile links in the csv file and store alumni info into respective csv files under resultSV directory.

## Run through newDBCreation notebook
This notebook contains steps of alumni database creation and manipulations.
