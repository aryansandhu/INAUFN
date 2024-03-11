from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    # chrome_options = Options()
    # # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

   
    # context.text_value = 10

# def after_step(context, step):
#     if step.status == "failed" or "passed":
#         allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    if scenario.status == "failed" or "passed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    
def after_all(context):
    context.driver.close()
