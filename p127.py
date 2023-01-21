from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/USER/Desktop/Python/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Proper name", "Bayer designation", "Distance(ly)", "Spectral class", "Mass(M)","Radius","Luminousity"]
    star_data = []
    for i in range(0,1):
        
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "brightest star"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_tag=li_tags[0]
            temp_list.append('https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'+hyperlink_tag.find_all('a',href=True)[0]['href'])
            star_data.append(temp_list)

       
    with open("star.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()