import os, random, sys, time
import argparse
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from termcolor import colored, cprint
from selenium.webdriver.chrome.options import Options
from win32com.client import Dispatch
import requests
import json

def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
versionfordriver = f'Drivers/{version.split(".")[0]}.exe'
print(versionfordriver)
# just uncomment this to run chrome in background.
options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome(executable_path=versionfordriver, options=options)
# browser = webdriver.Chrome(versionfordriver)
# https://www.linkedin.com/checkpoint/challenge/AgGznVM6JmTJWQAAAXpbY8tdfDNqvfH_PyvTqhnqsqwNovSBioedjejmQavHNKY0xWIjbW-QpinHZWYVZ345ZKIYlHdtGg?ut=0MWiPl78h8h9Q1
class Bot:

    def __init__(self, number_of_time_to_scroll=1):
        self.choice = 0
        self.base_url = 'https://www.linkedin.com'
        self.number_of_time_to_scroll = number_of_time_to_scroll

    def GetLinkedinCredentials(self,token):
        headers = {'Authorization':f'Token {token}',}
        response = requests.get('http://127.0.0.1:8000/api/GetLinkedinCredentials/',headers=headers)
        if response.status_code==200:
            return response.json()
        else:
            return "Error :  Token Incorrect or Linkedin Credentials Not Added"

    def login(self):
        global browser
        data = self.GetLinkedinCredentials(token=input("Enter your token ID : "))
        username = data['user']
        password = data['auth']
        print(username,password)
        browser.get(self.base_url + '/uas/login')
        emailElement = browser.find_element_by_id('username')
        emailElement.send_keys(username)
        passElement = browser.find_element_by_id('password')
        passElement.send_keys(password)
        passElement.submit()
        print(colored('Signing in...','blue', attrs=['reverse', 'blink']))
        time.sleep(4)
        print(colored('Signed in', 'green',attrs=['reverse', 'blink']))