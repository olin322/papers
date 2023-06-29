import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://openaccess.thecvf.com/CVPR2023?day=2023-06-21"

#If there is no such folder, the script will create one automatically
folder_location = "../Day2"
if not os.path.exists(folder_location):os.mkdir(folder_location)


response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    if (not os.path.isfile(filename)):
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
            print(filename.split('/')[-1])