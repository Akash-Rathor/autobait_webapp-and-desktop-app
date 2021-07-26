from login import Bot
from login import browser
from selenium.webdriver.common.action_chains import ActionChains
import time
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from termcolor import colored, cprint

if input('Do you want to follow user y/n : ').lower() =='y':
    follow = True
else:
    follow = False

message= input('Enter your message : ')
link_count = 0

def SendConnectionRequest():
    browser.refresh()
    with open('Collection.txt','r') as file_in:
        profilelinks = file_in.readlines()
    
    for link in profilelinks:
        time.sleep(3)
        # if link_count%5==0 and link_count<=45 and link_count<10:
        #     time.sleep(120)
        # if link_count>=10:
        if link_count%10==0 and link_count!=0 and link_count<=45:
            time.sleep(300)
        elif link_count>=45:
            return print(colored(f'Maximum Connection Requests Sent for the day, Total request sent -- > {link_count}', 'red', attrs=['reverse', 'blink']))
            # return print(f'Maximum Connection Requests Sent for the day, Total request sent -- > {link_count}')
        browser.get(link)
        # if str(browser.find_element_by_class_name('pvs-profile-actions ').find_element_by_class_name('artdeco-button__text').text) =='Connect':
        # print(browser.find_element_by_class_name('pvs-profile-actions ').text[0:7])
        if str(browser.find_element_by_class_name('pvs-profile-actions ').text[0:7]) =='Connect':
            if 'https://www.linkedin.com/premium/products/intent/?' not in browser.current_url:
                browser.find_element_by_class_name('pvs-profile-actions ').find_element_by_tag_name('button').click()
                addNotewhileConnect()

        else:
            browser.find_element_by_xpath("//span[text()='More']/..").click()
            # # to go to pop up connect button and click
            b2 = browser.find_elements_by_xpath("//div[contains(@id, ember) and contains(@class, 'display-flex align-items-center')]")
            for elem in b2:
                time.sleep(1)
                # if WebDriverWait(browser, 5).until(ExplicittwaitForElement(elem)):
                try:
                    if elem.find_element_by_tag_name('span').text == 'Connect':
                        ActionChains(browser).move_to_element(elem).click(elem).perform()

                        # #to add a note on pop up window
                        b3 = browser.find_element_by_xpath("//div[contains(@aria-labelledby, send-invite-modal) and contains(@class, 'send-invite')]")
                        b4 = b3.find_elements_by_tag_name('button')[1]
                        # b4 = b3.find_element_by_tag_name('button').find_element_by_xpath("//div[contains(@class, 'artdeco-button--muted artdeco-button--2')]")
                        if b4.text == 'Connect':
                            ActionChains(browser).move_to_element(b4).click(b4).perform()
                            addNotewhileConnect()

                    if follow:
                        if elem.find_element_by_tag_name('span').text == 'Follow':
                            print('Followed start')
                            ActionChains(browser).move_to_element(elem).click(elem).perform()
                            print('Followed Done')
                            time.sleep(3)
                except StaleElementReferenceException as Exception:
                    pass

def addNotewhileConnect():
    global link_count
    link_count+=1
    again = browser.find_element_by_xpath("//div[contains(@aria-labelledby, send-invite-modal) and contains(@class, 'send-invite')]")
    b4 = again.find_elements_by_tag_name('button')[1]
    if b4.text == 'Add a note':
        ActionChains(browser).move_to_element(b4).click(b4).perform()
        browser.find_element_by_tag_name('textarea').send_keys(message)
        #to click on send button
        browser.find_element_by_xpath("//div[contains(@aria-labelledby, send-invite-modal) and contains(@class, 'send-invite')]").find_elements_by_tag_name('button')[-1].click()
        return print(colored(f'Connection Request sent successfully, link no. - {link_count}', 'green', attrs=['reverse', 'blink']))
        # return print(f'Connection Request sent successfully, {link_count}')
    else:
        return print(colored(f'Connection Request failed @ link no. - {link_count}', 'red', attrs=['reverse', 'blink']))
        # return print('Connection Request failed')

# def ExplicittwaitForElement(elem):
#     element = elem
#     if element:
#         return element
#     else:
#         return False

# if __name__ == '__main__':
#     SendConnectionRequest