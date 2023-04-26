
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import json

import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stocks = []
    with open("Equity.csv", 'r') as csvequ:
        csvreader = csv.reader(csvequ)
        for x in csvreader:
            stocks.append(x[2])
        stocks.pop(0)
    op = webdriver.ChromeOptions()
    op.add_argument("headless")
    bro = webdriver.Chrome("chromedriver.exe",options=op)
    data1 = []
    i = 0
    erstocks = []
    for x in stocks:

        if i == 30:
            hout = json.dumps(data1)
            x = requests.post("http://127.0.0.1:5000/update", json=hout)
            print("sent")
            break
        else:
            try:
                d = []
                bro.get("https://www.bseindia.com/")
                bro.find_element_by_id("getquotesearch").send_keys(x)
                bro.find_element_by_id("getquotesearch").send_keys(Keys.RETURN)
                price = bro.find_element_by_id("idcrval").text
                eps = bro.find_elements_by_xpath('/html/body/div[1]/div[6]/div[3]/div/div[4]/div/table/tbody/tr[1]/td[2]')[0].text
                ceps = bro.find_elements_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[4]/div/table/tbody/tr[3]/td[2]")[0].text
                pe = bro.find_element_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[4]/div/table/tbody/tr[5]/td[2]").text
                pb = bro.find_element_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[4]/div/table/tbody/tr[7]/td[2]").text
                roe = bro.find_element_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[4]/div/table/tbody/tr[9]/td[2]").text
                group = bro.find_elements_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[5]/div/table/tbody/tr[3]/td[2]")[0].text
                industry = bro.find_elements_by_xpath("/html/body/div[1]/div[6]/div[3]/div/div[5]/div/table/tbody/tr[7]/td[2]")[0].text
                d.append(x)
                d.append(price)
                d.append(eps)
                d.append(ceps)
                d.append(pe)
                d.append(pb)
                d.append(roe)
                d.append(group)
                d.append(industry)
                data1.append(d)
                print(d)

            except:
                if  i == 30:
                    break
                print(x)
                erstocks.append(x)
                continue
        i = i + 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
