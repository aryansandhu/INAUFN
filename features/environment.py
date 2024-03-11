from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    context.driver = webdriver.Chrome()
    

def after_scenario(context, scenario):
    if scenario.status == "failed" or "passed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    
def after_all(context):
    context.driver.close()
