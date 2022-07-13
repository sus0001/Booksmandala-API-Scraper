# Booksmandala-API-Scraper:
The website has a hidden apis available. The scraper scrapes using requests module to api endpoints.

# Logic:
Below are the steps use by a scraper:                                                                                                                                   
⁍ Make request to API endpoint                                                                                                                                          
⁍ Read and fetch the data                                                                                                                                               
⁍ Check the number of pages available in the api endpoint.                                                                                                              
⁍ Download all the api content in a JSON format in a neatly created folder according to the category available in the website                                           
⁍ Extract all intended datas available in the downloaded json file and export into new single JSON or Excel format.                                                     
⁍ Give the User option to keep or delete the downloaded JSON file.                                                                                                      

I approach this step to avoid the unnecessary requests to API while extracting or playing around with datas.                                                              

# Instructions:
⁍ User will have to replace the path directory of the folder where they clone this repository.                                                                          
  •The path directory is variable named 'parent_directory' that is assigned in main_downloader_scraper.py file. User only have to replace the path directory of the folder where they clone this repository.               
⁍ User is greeted with availbale category of the Books available in the website with instructions:                                                                      
⁍ Enter the number according to the category and scraper will begin to download json file and export into the intended dataframes.                                      
⁍ After the scraping process. Scraper will ask the user to keep or delete the downloaded json file.                                                                     
⁍ After the command the scraper will exit.                                                                                                                              


# Package installation:                                                                                                                                                 
requests                                                                                                                                                                
pandas                                                                                                                                                                  
openpyxl                                                                                                                                                                
