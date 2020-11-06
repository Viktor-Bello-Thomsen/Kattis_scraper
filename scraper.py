from decouple import config
from selenium import webdriver
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait

def KattisLogin():
    driver.get("https://open.kattis.com/login/email?")
    driver.find_element_by_id("user_input").send_keys(email)
    driver.find_element_by_id("password_input").send_keys(password)
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.implicitly_wait(5)
    driver.get("https://open.kattis.com/problems?show_solved=on&show_tried=off&show_untried=off")

def turnPage():
    try:
        element = driver.find_element_by_id("problem_list_next").click()
        driver.implicitly_wait(5)
    except:
        return False
    return True

def scrapePage():
    elements = driver.find_elements_by_xpath("/html/body/div[1]/div/div/section/div[2]/table/tbody/tr/td[1]/a")
    problems = {}
    for i in elements:
        problems[i.text] = i.get_attribute('href')
    return problems

def getAlreadyScraped():
    names = set()
    try:
        with open("solved.txt", "r") as f:
            for line in f:
                names.add(line.strip())
    except:
        print("No previous Scrape detected")
    return names

def getNewProblems(seen, scraped):
    newProblems = set()
    for problemdID in scraped.keys():
        if problemdID not in seen:
            newProblems.add(problemdID)
    return newProblems

def downloadProblem(name, link):
    print(name, link)
    driver.get(link)
    driver.find_element_by_xpath("//*[@id="wrapper"]/div/div[2]/div[1]/section/div/div[2]/div/div/a").click()
    #Look at table and find solution with shortest time
    #click and get code and write to new txt file depending on code language



if __name__ == "__main__":
    #Login
    email = config('EMAIL')
    password = config('PASSWORD')
    driver = webdriver.Chrome()
    KattisLogin()
    #download name:link for all solved problems
    problems = {}
    while(True):
        problems.update(scrapePage())
        if not turnPage():
            break
    #get names of previously scraped problems
    priviousProblems = getAlreadyScraped()
    #find names not in priviousProblems
    newProblems = getNewProblems(priviousProblems, problems)
    #Handle each new problem
    for problemdID in newProblems:
        downloadProblem(problemdID, problems[problemdID])

    #Write names to solved.txt so we dont handle them again next scrape
    with open("solved.txt", "w+") as f:
        for name in sorted(problems):
            f.write(name+"\n")

    print(newProblems)
    driver.quit()
