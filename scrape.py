from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests

def send_telegram_message(message):
    TOKEN = "6682136449:AAEsM_l7Nc2jiOnNV0R1TeyOGOaVKD5ouIU"
    chat_id = "1217724954"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())

def scraper():
    while True:
        driver = Driver(uc=True, headless=True)
        driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")
        print("UA= ", driver.get_user_agent())
    
        bypassed = False
        
        while not bypassed:
            try:
                driver.send_keys("input[name='p_id_no']", "12108084")
                driver.send_keys("input[name='p_button']", Keys.RETURN)
                bypassed = True
            except Exception:
                print("Failed")
                driver.delete_all_cookies()
                driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")
        print("You're in")

        ## wala pa: arch2 lbyarch f
        courses = ["STADVDB", "GAMEDES", "CSARCH2", "LBYARCH"]
        preferred = [5789, 4411, 2383,  4306, 4307]
        dicts = [{"cc": 5789, "ct": "GAMEDES", "sched": "MH 1100 - 1230", "prof": "Ryan"},
                {"cc": 4411, "ct": "STADVDB", "sched": "TF 1245 - 1415", "prof": "Kerwin"},
                {"cc": 2383, "ct": "LBYARCH", "sched": "MH 1430 - 1600 ", "prof": "Laguna"},
                {"cc": 4306, "ct": "CSARCH2", "sched": "TF 1100 - 1230", "prof": "Roger"},
                {"cc": 4307, "ct": "CSARCH2", "sched": "MH 1430 - 1600", "prof": "Roger"}]

        try:
            print("Started scraping")
            while True:
                codes = []

                for course in courses:
                    driver.send_keys("input[name='p_course_code']", course)
                    driver.send_keys("input[name='p_button']", Keys.RETURN)

                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, 'html.parser')

                    font_elements = soup.find_all("font", {"color": "#006600"})

                    for font_element in font_elements:
                        bold_elements = font_element.find_all("b")

                        for bold_element in bold_elements:
                            text_content = bold_element.text
                            try:
                                number = int(text_content)

                                if number in preferred:
                                    codes.append(number)

                            except ValueError:
                                pass

                message = ""

                for code in codes:
                    for d in dicts:
                        if d["cc"] == code:
                            message += f"Code: {code}\nCourse: {d['ct']}\nSchedule: {d['sched']}\nProf: {d['prof']}\n\n"
                            print(message)

                if message != "":
                    send_telegram_message(message)

                time.sleep(15)
        except Exception: 
            print("Error encountered. Trying to restart")

if __name__ == "__main__":
    scraper()