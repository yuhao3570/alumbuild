from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, csv

# pattern of linkedin profile
AUTH = "www.linkedin.com/in/"

# to filter out search results without www.linkedin.com
def validate(searchResults):
    if searchResults is None:
        return searchResults

    results = [ ]
    for result in searchResults:
        p = result.find(AUTH)
        if p != -1:
            results.append(result[p:])
    return results

def searchDriver(headless):
    options = Options()
    if headless:
        options.add_argument('headless')
    options.add_argument("--normal")
    return webdriver.Chrome(chrome_options=options)

# parser to get search results
def parse(driver):
    results = []
    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        results.append(link.text.encode('utf-8').strip().decode())
    return validate(results)

# to concat name with possible links into one list
def concat(names, allResults):
    finalList = []
    for i in range(len(names)):
        finalList.append(names[i] + allResults[i])
    return finalList

# open up new_alum name file
inputfile = "/Users/hao/PycharmProjects/alumBuild/newNames.csv"
with open(inputfile) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    names = list(reader)

# to store all lists of links of each alum
allResults = []

driver=searchDriver(True)
for name in names:
    searchStr = str(name) + " " + "Mills College" + " linkedin"
    driver.get("https://www.google.com/search?q=" + searchStr)
    results = parse(driver)
    print(results)
    allResults.append(results)
    time.sleep(5)

with open("resultCSV/newLinks.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(concat(names, allResults))
