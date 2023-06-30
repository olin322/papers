import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import threading





def get_by_day(day):
    url = "https://openaccess.thecvf.com/CVPR2023?day=2023-06-2" + str(day - 1)
    #If there is no such folder, the script will create one automatically
    folder_location = "./Day" + str(day)
    if not os.path.exists(folder_location):os.mkdir(folder_location)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")     
    for link in soup.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        pdf_count = 0
        supp_count = 0
        if (not os.path.isfile(filename)):
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url,link['href'])).content)
                print(filename.split('/')[-1])
                def f(n):
                    match n:
                        case '0':
                            if (filename.find("supplemental.pdf") == -1):
                                pdf_count += 1
                                print("day 1: ", count, " / ", str(787))
                            else: 
                                supp_count += 1
                                print("day 1: ", supp_count, " / ", str(672))
                        case '1':
                            if (filename.find("supplemental.pdf") == -1):
                                pdf_count += 1
                                print("day 2: ", count, " / ", str(786))
                            else: 
                                supp_count += 1
                                print("day 2: ", supp_count, " / ", str(687))
                        case '2':
                            if (filename.find("supplemental.pdf") == -1):
                                pdf_count += 1
                                print("day 3: ", count, " / ", str(786))
                            else: 
                                supp_count += 1
                                print("day 3: ", supp_count, " / ", str(664))
                f(day)

def get_all():
    url = "https://openaccess.thecvf.com/CVPR2023?day=all"

    #If there is no such folder, the script will create one automatically
    folder_location = "../All"
    if not os.path.exists(folder_location):os.mkdir(folder_location)


    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")    
    pdf_count = 0
    supp_count = 0
    for link in soup.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        if (not os.path.isfile(filename)):
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url,link['href'])).content)
                print(filename.split('/')[-1])
                if (filename.find("supplemental.pdf") == -1):
                    pdf_count += 1
                    print("pdf: ", pdf_count, " / ", 2359)
                else:
                    supp_count += 1
                    print("supp: ", supp_count, " / ", 2023)




if __name__ == "__main__":
    t1 = threading.Thread(target = get_by_day, args = (1,))
    t2 = threading.Thread(target = get_by_day, args = (2,))
    t3 = threading.Thread(target = get_by_day, args = (3,))
    al = threading.Thread(target = get_all, args = ())

    t1.start()
    t2.start()
    t3.start()
    al.start()

    t1.join()
    t2.join()
    t3.join()
    al.join()