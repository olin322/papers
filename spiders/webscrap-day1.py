import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://openaccess.thecvf.com/CVPR2023?day=2023-06-20"

# If there is no such folder, the script will create one automatically
folder_location = "./Day1"
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")   
count = 0
pdf = 0
supp = 0 
err = 0
for link in soup.select("a[href$='.pdf']"):
    count += 1
    # Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    # if desired pdf file does not exist yet
    if (not os.path.isfile(filename)):
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
            print(filename.split('/')[-1])
    if (filename[-19:] == "CVPR_2023_paper.pdf"):
        pdf += 1
    elif (filename[-21:] == "2023_supplemental.pdf"):
        supp += 1
    else:
        err += 1
    print("file count:\t", count, " papers:\t", pdf, " supp:\t", supp, " err: ", err) 
    e = open("downloaded_papers_day1.csv", 'a')
    e.write(filename)
    e.close