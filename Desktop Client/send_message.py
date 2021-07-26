from login import browser
from login import Bot
import time
from termcolor import colored
Bot().login()

link_count = 0
class send_messages:

    def __init__(self,message):
        self.message=message
        

    def send_message(self,link):
        browser.get(link)
        if str(browser.find_element_by_class_name('pvs-profile-actions ').text[0:7]) =='Message':
            t = browser.find_element_by_class_name('v-align-middle').text.split()
            fname = t[0]
            lname = t[1]
            browser.find_element_by_class_name('pvs-profile-actions ').find_element_by_tag_name('a').click()
            browser.find_element_by_xpath("//div[contains(@class, msg-form__contenteditable) and contains(@contenteditable,'true')]").send_keys((self.message).format(fname=fname,lname=lname))
            # uncomment below line to send message
            time.sleep(1)
            browser.find_element_by_class_name("msg-form__send-button").click()
            browser.find_element_by_xpath("//button[contains(@class, msg-artdeco-button--1) and contains(@data-control-name,'overlay.close_conversation_window')]").click()
            print(f'Message successfully sent to {fname} {lname}'.format(fname=fname,lname=lname))
        else:
            pass

with open('Collection.txt','r') as file_in:
    profilelinks = file_in.readlines()
    for link in profilelinks:
        if link_count%10==0 and link_count!=0 and link_count<=45:
            time.sleep(300)
        elif link_count>=45:
            print(colored(f'Maximum Connection Requests Sent for the day, Total request sent -- > {link_count}', 'red', attrs=['reverse', 'blink']))
        else:
            time.sleep(5)
            send_messages("Hi {fname} {lname}, Thanks! for connecting!").send_message(link)
            link_count+=1