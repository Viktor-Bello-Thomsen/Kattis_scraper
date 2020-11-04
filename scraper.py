from decouple import config
from selenium import webdriver
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

def handlePage():
    elements = driver.find_elements_by_xpath("/html/body/div[1]/div/div/section/div[2]/table/tbody/tr/td[1]/a")
    problems = []
    for i in elements:
        problems.append(i.text)
    return problems


if __name__ == "__main__":
    email = config('EMAIL')
    password = config('PASSWORD')
    driver = webdriver.Chrome()

    KattisLogin()
    running = True
    names = []
    while(running):
        names.extend(handlePage())
        running = turnPage()

    with open("solved.txt", "w") as f:
        for name in names:
            f.write(name+"\n")
    driver.quit()
