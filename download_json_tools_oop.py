import json
import time
import pprint
import requests
import random


def get_ua():
    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 "
        "Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 "
        "Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 "
        "Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
    ]
 
    return random.choice(uastrings)

url = "https://booksmandala.com/api/books?page=1&main_category=sports"
json_name = "fiction and literature"
# api_pages = Booksmandala(booksmandala_base_api).read_api_call()




class DownloadJSON:
    def __init__(self, api_url):
        self.headers = {"User-Agent": get_ua()}
        self.api_url = api_url
        self.req = requests.get(api_url, headers=self.headers)
    

    def total_api_pages(self):
        call_content = json.loads(self.req.content)
        last_page = call_content['links']['last'].split("=")[-1]
        
        return int(last_page) 

    
    def download_file(self, pageNum, json_name, json_folder):
        self.json_folder = json_folder
        self.json_name = json_name
        api_call = self.req.content
        
        try:
            with open(f"{json_folder}\\{json_name} {pageNum}.json", 'wb') as f:
                f.write(api_call)
            
            print(f"Saved | {json_name} JSON | Page Number: {pageNum}.\n----------------------------------")
        except requests.JSONDecodeError:
            print("Unauthorised access!")



    
class ReadJSON:
    def __init__(self, path_lists):
        self.path_lists = path_lists
        

        
    def read_json(self, folder_name): 
        with open(f"{folder_name}\\{self.path_lists}", 'r') as jsn:
            api_call = json.load(jsn)
        
        return api_call