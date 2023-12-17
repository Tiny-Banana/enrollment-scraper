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
    driver = Driver(uc=True)
    driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")
    print("UA= ", driver.get_user_agent())
    
    bypassed = False
    
    while not bypassed:
        try:
            driver.send_keys("input[name='p_id_no']", "12108084")
            driver.send_keys("input[name='p_button']", Keys.RETURN)
            bypassed = True
        except Exception:
            driver.delete_all_cookies()
            driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")

    courses = ["STSWENG", "3DMODEL", "CSARCH2", "LBYARCH", "STADVDB", "GAMEDES", "HCI2001", "GEWORLD", "MOBDEVE"]
    preferred = [5789, 6212, 6213, 4307, 4306]
    dicts = [{"cc": 5789, "ct": "GAMEDES", "sched": "MH 1100 - 1230", "prof": "Ryan Dimaunahan"},
            {"cc": 6212, "ct": "HCI2001", "sched": "MH 0730 - 0900", "prof": "Jordan"},
            {"cc": 6213, "ct": "HCI2001", "sched": "M 0730 - 0900 H 0915 - 1045", "prof": "Jordan"},
            {"cc": 4307, "ct": "CSARCH2", "sched": "MH 1430 - 1600", "prof": "Roger"},
            {"cc": 4306, "ct": "CSARCH2", "sched": "TF 1100 - 1200", "prof": "Roger"}]

    while True:
        codes = []
        for course in courses:
            driver.send_keys("input[name='p_course_code']", course)
            driver.send_keys("input[name='p_button']", Keys.RETURN)

            time.sleep(0.5)

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

        time.sleep(10)

if __name__ == "__main__":
    scraper()