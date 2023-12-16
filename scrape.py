"""Determine if your browser is detectable by anti-bot services.
Some sites use scripts to detect Selenium, and then block you.
To evade detection, add --uc as a pytest command-line option."""
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from email.message import EmailMessage
import time
import smtplib

BaseCase.main(__name__, __file__, "--uc", "-s")


class UndetectedTest(BaseCase):

    def test_browser_is_undetected(self):
        if not (self.undetectable):
            self.get_new_driver(undetectable=True)
        self.driver.get("https://enroll.dlsu.edu.ph/dlsu/view_course_offerings/#relax")
        
        time.sleep(1)
        print(self.driver.page_source)
        # idnum = self.get_element("input[name='p_id_no']")
        # idnum.send_keys("12108084")
        # idnum.send_keys(Keys.RETURN)
        
        # courses = ["STSWENG", "3DMODEL", "CSARCH2", "LBYARCH", "STADVDB", "GAMEDES", "GEARTAP", "GEWORLD"]
        # avail = {}

        # for course in courses:
        #     avail.update({"course": course})
        #     print("\n\n" + course + "\n\n")
            
        #     cc = self.get_element("input[name='p_course_code']")
        #     cc.send_keys(course)
        #     cc.send_keys(Keys.RETURN)

        #     time.sleep(1)

        #     page_source = self.driver.page_source
        #     soup = BeautifulSoup(page_source, 'html.parser')

        #     font_elements = soup.find_all("font", {"color": "#006600"})
        #     codes = []

        #     # Iterate through each <font> element and get the <b> elements inside them
        #     for font_element in font_elements:
        #         bold_elements = font_element.find_all("b")

        #         # Process the bold elements as needed
        #         for bold_element in bold_elements:
        #             # Extract information or perform actions on the bold element
        #             text_content = bold_element.text
        #             # Attempt to convert the text content to an integer
        #             try:
        #                 number = int(text_content)
        #                 # Print only if conversion is successful
        #                 codes.append(number)
        #                 print(number)
        #             except ValueError:
        #                 # Handle the case where conversion to integer fails (e.g., text contains non-numeric characters)
        #                 pass
        #     avail.update({"codes": codes})



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


# if __name__ == '__main__':
#     email_alert("Hey", "Hello world", "deifymichiru@gmail.com")