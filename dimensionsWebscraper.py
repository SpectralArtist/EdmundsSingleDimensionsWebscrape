from bs4 import BeautifulSoup
import requests
import json
import time

make = input("Enter a Make: ")
model = input("Enter a Model: ")
year = input("Enter Year: ")
print("")

url = "https://www.edmunds.com/" + make + "/" + model + "/" + year + "/features-specs/"

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
content = BeautifulSoup(response.content, "html.parser")
tables = content.find_all('table')
dimensionsTable = ""

for table in tables:
    if (table.find('caption').text == "Dimensions"):
        dimensionsTable = table

tableHeaders = dimensionsTable.find_all('th')
tableData = dimensionsTable.find_all('td')

for i in range(1, len(tableHeaders)):
    measurement = ""
    if "in." in tableData[i - 1].text:
        value = float(tableData[i - 1].text.split(' ')[0])
        feet = int(value / 12)
        inches = value % 12
        measurement = str(feet) + " ft. " + str(round(inches, 1)) + " in."
        print ("{0:20} {1}".format(tableHeaders[i].text, measurement))
    else:
        print ("{0:20} {1}".format(tableHeaders[i].text, tableData[i - 1].text))


