import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://openaccess.thecvf.com/CVPR2023?day=all"

#If there is no such folder, the script will create one automatically
// folder_location = "./AllPapers"
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
count = 0
pdf = 0
supp = 0
err = 0
soup = BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    count += 1
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    # print(filename[-19:])
    # print(filename[-21:])
    # break
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
    # t = link['href'].split('/')[-1]
    # t = t[t.find('_') + 1:]
    # print(t)
    # filename = os.path.join(folder_location,t)
    # with open(filename, 'wb') as f:
    #     f.write(requests.get(urljoin(url,link['href'])).content)
    # print(filename.split('/')[-1])

## total files expected: 2359 + 2023
