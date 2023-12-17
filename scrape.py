# from seleniumbase import BaseCase
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# from email.message import EmailMessage
# import time
# import smtplib
# import requests

# BaseCase.main(__name__, __file__, "--uc", "-s")

# class UndetectedTest(BaseCase):

#     def test_browser_is_undetected(self):
#         if not (self.undetectable):
#             self.get_new_driver(undetectable=True, headed=True)
#         self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {
#     "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# })
#         self.driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/#relax")
        
#         idnum = self.get_element("input[name='p_id_no']")
#         idnum.send_keys("12108084")
#         idnum.send_keys(Keys.RETURN)
        
#         courses = ["STSWENG", "3DMODEL", "CSARCH2", "LBYARCH", "STADVDB", "GAMEDES", "HCI2001", "GEWORLD", "MOBDEVE"]
#         preferred = [5789, 6212, 6213, 4307, 4306]
#         dicts = [{"cc": 5789, "ct": "GAMEDES", "sched": "MH 1100 - 1230", "prof": "Ryan Dimaunahan"},
#                 {"cc": 6212, "ct": "HCI2001", "sched": "MH 0730 - 0900", "prof": "Jordan"},
#                 {"cc": 6213, "ct": "HCI2001", "sched": "M 0730 - 0900 H 0915 - 1045", "prof": "Jordan"},
#                 {"cc": 4307, "ct": "CSARCH2", "sched": "MH 1430 - 1600", "prof": "Roger"},
#                 {"cc": 4306, "ct": "CSARCH2", "sched": "TF 1100 - 1200", "prof": "Roger"}]

#         while True:
#             codes = []
#             for course in courses:
#                 # print("\n\n" + course + "\n\n")
                
#                 cc = self.get_element("input[name='p_course_code']")
#                 cc.send_keys(course)
#                 cc.send_keys(Keys.RETURN)

#                 time.sleep(0.5)

#                 page_source = self.driver.page_source
#                 soup = BeautifulSoup(page_source, 'html.parser')

#                 font_elements = soup.find_all("font", {"color": "#006600"})

#                 # Iterate through each <font> element and get the <b> elements inside them
#                 for font_element in font_elements:
#                     bold_elements = font_element.find_all("b")

#                     # Process the bold elements as needed
#                     for bold_element in bold_elements:
#                         # Extract information or perform actions on the bold element
#                         text_content = bold_element.text
#                         # Attempt to convert the text content to an integer
#                         try:
#                             number = int(text_content)

#                             # Print only if conversion is successful
#                             if number in preferred:
#                                 codes.append(number)
        
#                             # print(number)
#                         except ValueError:
#                             # Handle the case where conversion to integer fails (e.g., text contains non-numeric characters)
#                             pass
            
#             message = ""

#             for code in codes:
#                 for d in dicts:
#                     if d["cc"] == code:
#                         message += f"Code: {code}\nCourse: {d["ct"]}\nSchedule: {d["sched"]}\nProf: {d["prof"]}\n\n"
#                         print(message)
            
#             if message != "":
#                 send_telegram_message(message)
#                 # email_alert("Available Preferred Courses!", message, "alerts.notify.now.me@gmail.com")

#             time.sleep(10)
            
# def send_telegram_message(message):
#     TOKEN = "6682136449:AAEsM_l7Nc2jiOnNV0R1TeyOGOaVKD5ouIU"
#     chat_id = "1217724954"
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
#     print(requests.get(url).json())


# def email_alert(subject, body, to):
#     msg = EmailMessage()
#     msg.set_content(body)
#     msg['subject'] = subject
#     msg['to'] = to

#     user = "deifymichiru@gmail.com"
#     msg['from'] = user
#     password = "gagjbbisfcmhwohd"

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(user, password)
#     server.send_message(msg)

#     server.quit()


# from seleniumbase import Driver
# from selenium.webdriver.common.keys import Keys

# driver = Driver(uc=True, headed=True)
# driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/")
# print("UA= ", driver.get_user_agent())

# driver.type("input[name='p_id_no']", "12108084")
# driver.click("input[name='p_button']")

#try
from seleniumbase import BaseCase

class MyTest(BaseCase):

    def test_example(self):
        self.open("https://example.com")