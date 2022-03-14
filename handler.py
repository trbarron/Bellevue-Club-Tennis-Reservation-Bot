import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from philPasswords import userPass

actualHour = 8
actualMinute = 45

def checkTennis():
    URL = 'https://members.bellevueclub.com/group/pages/tennis-court-reservations'
    # BC credentials
    username = userPass.username
    password = userPass.password

    # initialize the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


    s = Service('./chromedriver.exe')

    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # head to github login page
    driver.get(URL)
    # find username/email field and send the username itself to the input field
    driver.find_element(By.ID, "_58_login").send_keys(username)
    # find password input field and insert password as well
    driver.find_element(By.ID, "_58_password").send_keys(password)
    # click login button
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )


    driver.find_element(By.CSS_SELECTOR, ".fa-angle-double-right").click()
    
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    time.sleep(3)


    # Wait until 8:ac on the dot
    currentTime = datetime.now()
    tryCounter = 0
    while not (currentTime.hour == actualHour and currentTime.minute == actualMinute and tryCounter < 2000):
        time.sleep(1)
        currentTime = datetime.now()
        # isTimerActive = driver.find_elements(By.CSS_SELECTOR, ".advance-booking-overlay")

        tryCounter += 1

    time.sleep(1)



        # Monday- 8:30 PM Slot
        # Tuesday- 7:15 PM Slot
        # Friday: 3:30 PM Slot
        # Sunday: 1PM slot 

    # Sleep just to make sure it is all good

    currentDay = datetime.today().weekday()
    
    timeOfInterest = None
    selection = None
    
    if currentDay == 0: #0 = Monday
        timeOfInterest = "06:00 PM"

    elif currentDay == 1: #1 = Tuesday
        timeOfInterest = "07:15 PM"

    elif currentDay == 4: #4 = Friday
        timeOfInterest = "03:30 PM"

    elif currentDay == 6: #6 = Sunday
        timeOfInterest = "01:00 PM"

    else:
        return

    w = driver.find_elements(By.CSS_SELECTOR, ".interval")
    for i in w:
        if i.text == timeOfInterest:
            c = i
    p = c.find_element(By.XPATH, '..')
    m = p.find_elements(By.CSS_SELECTOR, ".slot")
            
    try:
        indoor1 = m[0]
        indoor2 = m[1]
        indoor3 = m[2]
        indoor4 = m[3]
        indoor5 = m[4]
        indoor6 = m[5]

    except:
        indoor1 = None
        indoor2 = None
        indoor3 = None
        indoor4 = None
        indoor5 = None
        indoor6 = None
    
    if indoor1.text == "" and 'open' in indoor1.get_attribute("class"):
        selection = indoor1
    elif indoor2.text == "" and 'open' in indoor2.get_attribute("class"):
        selection = indoor2
    elif indoor3.text == "" and 'open' in indoor3.get_attribute("class"):
        selection = indoor3
    elif indoor4.text == "" and 'open' in indoor4.get_attribute("class"):
        selection = indoor4
    elif indoor5.text == "" and 'open' in indoor5.get_attribute("class"):
        selection = indoor5
    elif indoor6.text == "" and 'open' in indoor6.get_attribute("class"):
        selection = indoor6

    while selection:

        failCounter = 0

        try:
            selection.click()

            WebDriverWait(driver=driver, timeout=10).until(
                lambda x: x.execute_script("return document.readyState === 'complete'")
            )
            time.sleep(10)

            m = driver.find_elements(By.CSS_SELECTOR, ".ui-button-text")

            for c in m:
                if c.text == "Save":
                    c.click()
                    print("!!!!!!!!!!!!!!!!!!")
                    print("!!!!!!!!!!!!!!!!!!")
                    print("!!!!!!!!!!!!!!!!!!")
                    print("Got a reservation!")
                    print("At time: ", datetime.now())
                    print("!!!!!!!!!!!!!!!!!!")
                    print("!!!!!!!!!!!!!!!!!!")
                    print("!!!!!!!!!!!!!!!!!!")

            # driver.close()
            time.sleep(23 * 60 * 60) # Sleep 23 hours so you don't double trigger on that day
        except:
            time.sleep(0.01)
            failCounter += 1
        
        if failCounter > 10000:
            continue

    try:
        driver.close()
        print("did not get a reservation: ")
        print("At time: ", datetime.now())
        
    except:
        print('already closed')

if __name__ == '__main__':
    print("... Sleeping...")
    while True:
        currentTime = datetime.now()
        if currentTime.hour == actualHour and currentTime.minute >= (actualMinute - 1) and currentTime.minute <= (actualMinute + 1):
            checkTennis()
        else: 
            time.sleep(1)
            