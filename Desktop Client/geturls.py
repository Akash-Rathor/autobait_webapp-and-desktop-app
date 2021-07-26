from search import search_people
from bs4 import BeautifulSoup as bs
import selenium
import lxml
import io,os
import time
import numpy as np
from login import browser

class GetClearURLs(search_people):
    
    def __init__(self,*args,**kwargs):
        super(GetClearURLs,self).__init__(*args, **kwargs)

    def CollectProfileUrls(self):
        from login import browser
        #this is to limit the page change currently its only 10 pages
        for _ in range(1,10):
            time.sleep(4)
            self.search(_)
            soup = bs(browser.page_source,'lxml')
            urls = [t.find('a',{'class':'app-aware-link'}) for t in [a.find('div',{'class':'display-flex'}) for a in soup.find_all('div',{'class':'t-roman t-sans'})]]
            print(urls[0])
            with io.open('output.txt','a',encoding="utf-8") as file_out:
                # storing each profile url in a file.
                for i in urls:
                    file_out.write(i.get('href')+'\n')
        self.ClearUrls()

    def ClearUrls(self):
        print('Clearing URLs')
        with open('output.txt') as file_in:
            content = file_in.readlines()
            browser.refresh()
            content = np.unique(content).tolist()
            # content = list(set(content))
            for _ in content:
                if 'headless?' in _ or 'premium' in _:
                    content.remove(_)
        try:
            browser.refresh()
            os.remove('Collection.txt')
        except:
            pass

        os.remove('output.txt')
        with open('Collection.txt','a') as file_out:
            browser.refresh()
            for _ in content:
                file_out.write(_)
        print('Clearning Url Done')
        