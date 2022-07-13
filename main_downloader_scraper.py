import time
import pprint
import pandas as pd
from pandas import read_json
from download_json_tools_oop import DownloadJSON, ReadJSON
import os
import shutil
import winsound
import sys
import json
import winsound


# track the timer:
start_time = time.time() 
base_api_url = "https://booksmandala.com/api/books?page=1&main_category="

# Time interval between each requests. Decrease time interval for faster scraping, however I discourage you to do so as it may hurt the server or throw an error: I've set the default value to 2 seconds:
request_interval = 2

# Category available in Booksmandala:
category_dict = {
    '1': 'fiction-&-literature',
    '2': 'lifestyle-&-wellness',
    '3': 'academic-&-reference',
    '4': 'religion-&-mythology',
    '5': 'art-&-design',
    '6': 'biography-&-memoir',
    '7': 'general-non-fiction',
    '8': 'business-&-finance',
    '9': 'poetry-&-plays',
    '10': 'sports',
    '11': 'self-development-&-motivation',
    '12': 'travel,-atlas',
    '13': 'kids-and-teens',
    '14': 'graphic-novels'

}


# Pretty print the output console:
pp = pprint.PrettyPrinter()

# Initialzing an empty string for user input:
user_input = ""
new_api_url = ""


# Greeting message
print(f"Welcome to Booksmandala Scraper. Below are the key to scrape different categories available in the website.\n----------------------------------------------------------------------------------------------------------")
pp.pprint(category_dict)


# Setting an infinite loop unless user input a certain instruction to run the program:
while True:  
    time.sleep(2)
    # print("-----------------------------------------------------------------------------")
    user_input = input("Enter a category number:> ")
    print("-----------------------------------------------------------------------------")
    dict_key_response = category_dict.get(user_input)
   
    if user_input == 'cat':
        pp.pprint(category_dict)
    elif user_input == 'q':
        print(f"Exiting. Thank you for using BooksmandalaWeb Scraper.")
        sys.exit()
    elif dict_key_response is None:
        print("Wrong input! \n----------------------------------\nEnter a value between 1 and 14\nType 'cat' to view the category\nType 'q' to exit:\n-----------------------------------")
    
    else:
        print(f"Category | {dict_key_response}\n--------------------------------------")        
        user_input = f"{base_api_url}{dict_key_response}"
        break
        
 
# Calculation the total number pages per categor available in the API:
total_pages = DownloadJSON(user_input).total_api_pages()
json_name = dict_key_response


# Creating a separate directory to store downloaded file:
folder_directory = " ".join(dict_key_response.split("-"))
parent_dir = 'C:\\Users\\rocki\\Py\\download_json'
path_dir = os.path.join(parent_dir, folder_directory)


# Overwriting the created directory if its already existed
if os.path.exists(path_dir):
    shutil.rmtree(path_dir)
os.mkdir(path_dir)


print(f"There are {total_pages} pages.\n---------------------------")
for i in range(1, total_pages+1):
    time.sleep(2)
    url = f"https://booksmandala.com/api/books?page={str(i)}&main_category={user_input}"
    DownloadJSON(url).download_file(i, json_name, path_dir)
    
    
time.sleep(2)
print(f"Saved!")

print("Fetching data from downloaded Json file.")
time.sleep(2)


# paste your path url below: c:\\users\\yourusername\\and so on
path_lists = os.listdir(f'c:\\users\\rocki\\Py\\download_json\\{folder_directory}')


# Function to iterate and extract data. I couldn't implement this logic via OOP for now.
def data_in_dict():
    books_name  = []
    books_isbn = []
    books_author = []
    books_sale_price = []
    books_description = []
    books_publisher = []
    books_publishion_date = []
    books_image_url = []
    books_link = []
    for path in path_lists:
        try:
            for d in range(18):
                booksmandala = ReadJSON(path)
                name = booksmandala.read_json(folder_directory)['data'][d]['name']
                isbn = booksmandala.read_json(folder_directory)['data'][d]['sku']
                author = booksmandala.read_json(folder_directory)['data'][d]['author']
                sale_price = booksmandala.read_json(folder_directory)['data'][d]['sale_price']
                description = booksmandala.read_json(folder_directory)['data'][d]['description']
                publisher = booksmandala.read_json(folder_directory)['data'][d]['publisher']
                publishion_date = booksmandala.read_json(folder_directory)['data'][d]['published_at']
                link = booksmandala.read_json(folder_directory)['data'][d]['shareable_url']
                image = booksmandala.read_json(folder_directory)['data'][d]['thumbnail_url']

                books_name.append(name)
                books_author.append(author)
                books_isbn.append(isbn)
                books_author.append(author)
                books_sale_price.append(sale_price)
                books_description.append(description)
                books_publisher.append(publisher)
                books_publishion_date.append(publishion_date)
                books_link.append(link)
                books_image_url.append(image)
                print(name)
        except IndexError:
            continue
    
    # Storing all the collected items in dictionary:
    dicts = {
        "Name": books_name,
        "ISBN": books_isbn,
        "Sale Price": books_sale_price,
        "Description": books_description,
        "Publisher": books_publisher,
        "Publishion date": books_publishion_date,
        "Book URL": books_link,
        "Book Image URL": books_image_url
    }

    return dicts


# Exporting data via pandas dataframe:
df = pd.DataFrame(data_in_dict())
df.to_json(f"{folder_directory}.json", indent=4)
df.to_excel(f"{folder_directory}.xlsx", index=False)
print("Saved\n----------------------------------------")


# Give the user option to keep or delete the downloaded Json file including the folder:
user_input_2 = ""
while True:    
    user_input_2 = input("Do you want to save the JSON folder?\n--------------------------------------------\nType 'y' for yes or 'n' for no\n:> ")
    print(f"Wrong input. Type 'y' for yes or 'n' for no.")

    if user_input_2 == 'y':
        print(f"Saving....")
        break
    elif user_input_2 == 'n':
        shutil.rmtree(path_dir)
        print(f"Deleting....\n------------------------------")
        break
    else:
        continue
time_took = time.time() - start_time


# Play sound after completion:
winsound.PlaySound('notificaton.mp3', winsound.SND_FILENAME)


print(f'Took {round(time_took, 2)} seconds....')
print(f"Tool {round(time_took/60, 2)} minutes....")
