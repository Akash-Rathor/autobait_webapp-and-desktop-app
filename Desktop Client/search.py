
from login import Bot
import re

class search_people:
    
    def __init__(self,url):
        self.base_url = url
        Bot().login()

    def GenerateUrl(self,n):
        linkedin_Search_base_url = self.base_url
        if 'FACETED_SEARCH&' in linkedin_Search_base_url:
            val = re.search('FACETED_SEARCH&',linkedin_Search_base_url).span()
            # print(linkedin_Search_base_url[:val[1]-1]+f'&page={n}&'+linkedin_Search_base_url[:val[1]+len(f'&page={n}&')])
            return linkedin_Search_base_url[:val[1]-1]+f'&page={n}&'+linkedin_Search_base_url[:val[1]+len(f'&page={n}&')]
        elif 'SWITCH_SEARCH_VERTICAL' in linkedin_Search_base_url or 'FACETED_SEARCH' in linkedin_Search_base_url or 'CLUSTER_EXPANSION' in linkedin_Search_base_url:
            return f'{linkedin_Search_base_url}&page={n}'

    def search(self,n):
        from login import browser
        if self.GenerateUrl(n) != 'URL Incorrect':
            browser.get(self.GenerateUrl(n))