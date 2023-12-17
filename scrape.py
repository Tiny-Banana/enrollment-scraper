# from seleniumbase import Driver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time
# import requests

# def send_telegram_message(message):
#     TOKEN = "6682136449:AAEsM_l7Nc2jiOnNV0R1TeyOGOaVKD5ouIU"
#     chat_id = "1217724954"
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
#     print(requests.get(url).json())

# def scraper():
#     driver = Driver(uc=True, headless=True)
#     driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")
#     print("UA= ", driver.get_user_agent())

#     driver.send_keys("input[name='p_id_no']", "12108084")
#     driver.send_keys("input[name='p_button']", Keys.RETURN)

#     courses = ["STSWENG", "3DMODEL", "CSARCH2", "LBYARCH", "STADVDB", "GAMEDES", "HCI2001", "GEWORLD", "MOBDEVE"]
#     preferred = [5789, 6212, 6213, 4307, 4306]
#     dicts = [{"cc": 5789, "ct": "GAMEDES", "sched": "MH 1100 - 1230", "prof": "Ryan Dimaunahan"},
#             {"cc": 6212, "ct": "HCI2001", "sched": "MH 0730 - 0900", "prof": "Jordan"},
#             {"cc": 6213, "ct": "HCI2001", "sched": "M 0730 - 0900 H 0915 - 1045", "prof": "Jordan"},
#             {"cc": 4307, "ct": "CSARCH2", "sched": "MH 1430 - 1600", "prof": "Roger"},
#             {"cc": 4306, "ct": "CSARCH2", "sched": "TF 1100 - 1200", "prof": "Roger"}]

#     while True:
#         codes = []
#         for course in courses:
#             driver.send_keys("input[name='p_course_code']", course)
#             driver.send_keys("input[name='p_button']", Keys.RETURN)

#             time.sleep(0.5)

#             page_source = driver.page_source
#             soup = BeautifulSoup(page_source, 'html.parser')

#             font_elements = soup.find_all("font", {"color": "#006600"})

#             for font_element in font_elements:
#                 bold_elements = font_element.find_all("b")

#                 for bold_element in bold_elements:
#                     text_content = bold_element.text
#                     try:
#                         number = int(text_content)

#                         if number in preferred:
#                             codes.append(number)

#                     except ValueError:
#                         pass

#         message = ""

#         for code in codes:
#             for d in dicts:
#                 if d["cc"] == code:
#                     message += f"Code: {code}\nCourse: {d['ct']}\nSchedule: {d['sched']}\nProf: {d['prof']}\n\n"
#                     print(message)

#         if message != "":
#             send_telegram_message(message)

#         time.sleep(10)

# scraper()



"""Determine if your browser is detectable by anti-bot services.
Some sites use scripts to detect Selenium, and then block you.
To evade detection, add --uc as a pytest command-line option."""
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc", "-s")


class UndetectedTest(BaseCase):
    def verify_success(self):
        self.assert_text("OH YEAH, you passed!", "h1", timeout=6.25)
        self.post_message("Selenium wasn't detected!", duration=2.8)
        self._print("\n Success! Website did not detect Selenium! ")

    def fail_me(self):
        self.fail('Selenium was detected! Try using: "pytest --uc"')

    def test_browser_is_undetected(self):
        if not (self.undetectable):
            self.get_new_driver(undetectable=True, headless=True)
        self.driver.get("https://nowsecure.nl/#relax")
        try:
            self.verify_success()
        except Exception:
            self.clear_all_cookies()
            self.get_new_driver(undetectable=True, headless=True)
            self.driver.get("https://nowsecure.nl/#relax")
            try:
                self.verify_success()
            except Exception:
                if self.is_element_visible('iframe[src*="challenge"]'):
                    with self.frame_switch('iframe[src*="challenge"]'):
                        self.click("span.mark")
                else:
                    self.fail_me()
                try:
                    self.verify_success()
                except Exception:
                    self.fail_me()