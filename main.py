import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime

dateStyle = xlwt.easyxf(num_format_str='HH:MM, DD-MMM-YYYY')
appliedStyle = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

rb = xlrd.open_workbook('jobs.xls',formatting_info=True)
rs = rb.sheet_by_index(0) 
row = rs.nrows

wb = copy(rb) 
ws = wb.get_sheet(0) 

URL='https://www.monster.ca/jobs/search/?q=Software-Engineer-intern&where=Toronto__2C-Canada-&jobid=b697209f-417b-4e67-8ac5-e19487dc85b0'
# URL='https://ca.indeed.com/jobs?q=software%20engineer%20intern&l=Toronto%2C%20ON&vjk=4fb9ee159ff25c91'
page=requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
results=soup.find(id='ResultsContainer')
jobElements=results.find_all('section', class_='card-content')

for elem in jobElements:

    if((elem.find('h2', string=lambda text: 'intern' in text.lower()) is None) and (elem.find('h2', string=lambda text: 'developer' in text.lower()) is None)):
        continue

    linkElem = elem.find('a')
    titleElem = elem.find('h2', class_='title')
    companyElem= elem.find('div', class_='company')
    locationElem = elem.find('div', class_='location')
    timeElem =elem.find('time')

    if None in (linkElem, titleElem, companyElem, locationElem,timeElem):
        continue

    link=linkElem['href']
    title=titleElem.text.strip()
    company=companyElem.text.strip()
    location= locationElem.text.strip()
    time=timeElem.text.strip()

    ws.write(row, 0, time)
    ws.write(row, 1, title)
    ws.write(row, 2, company)
    ws.write(row, 3, location)
    ws.write(row, 4, link)
    ws.write(row, 5, datetime.now(), dateStyle)
    ws.write(row, 6, 'Not Applied', appliedStyle)

    row+=1

wb.save('jobs.xls')

