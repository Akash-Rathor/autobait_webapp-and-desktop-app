view = input('Do You want to View Profile y/n : ').lower()
connect = input('Do You want send connection request y/n : ').lower()

from geturls import GetClearURLs
import send_connection
import view_profile
from login import browser

from win32com.client import Dispatch

n = 0
def takeurlinput():
    global n
    url = input('Enter the filtered URL with minimum 500 + results : ')
    if 'FACETED_SEARCH&' in url or 'FACETED_SEARCH' in url or'SWITCH_SEARCH_VERTICAL' in url and 'page' not in url:
        GetClearURLs(url).CollectProfileUrls()
        if view=='y' and connect=='n':
            view_profile.ViewProfile()
        if connect=='y':
            send_connection.SendConnectionRequest()
    else:
        print(f'''URL Incorrect! ----> Please enter Correct URL
                {3-n} attempt left''')
        n+=1
        if n<4:
            takeurlinput()
        else:
            'Sorry you tried maximum attempt to enter correct URL'
takeurlinput()


browser.quit()

