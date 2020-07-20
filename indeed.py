import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime

def findJobs():
    dateStyle = xlwt.easyxf(num_format_str='HH:MM, DD-MMM-YYYY')
    appliedStyle = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

    rb = xlrd.open_workbook('jobs.xls',formatting_info=True)
    rs = rb.sheet_by_index(0) 
    row = rs.nrows

    wb = copy(rb) 
    ws = wb.get_sheet(0) 

    URL='https://ca.indeed.com/jobs?q=software+engineer+intern&l=Toronto%2C+ON'
    page=requests.get(URL)

    soup=BeautifulSoup(page.content, 'html.parser')
    results=soup.find(id='resultsCol')
    jobElements=results.find_all('div', class_='result')

    for elem in jobElements:

        titleElem = elem.find('a', class_='jobtitle')

        if(('engineer' not in titleElem.text.strip().lower().split(" ")) and ('developer' not in titleElem.text.strip().lower().split(" "))):
            continue

        linkElem = elem.find('a')
        titleElem = elem.find('a', class_='jobtitle')
        companyElem= elem.find('span', class_='company')
        locationElem = elem.find('span', class_='location')
        timeElem =elem.find('span', class_='date')

        if None in (linkElem, titleElem, companyElem, locationElem,timeElem):
            continue

        link=linkElem['href']
        title=titleElem.text.strip()
        company=companyElem.text.strip()
        location= locationElem.text.strip()
        time=timeElem.text.strip()

        if(link[0:7]!="/rc/clk"):
            continue

        newLink=link.replace("/rc/clk", "https://ca.indeed.com/viewjob")
        cutOff=newLink.index("&")
        end=len(newLink)-1
        newLink = newLink[0: cutOff:] + newLink[end + 1::]

        ws.write(row, 0, time)
        ws.write(row, 1, title)
        ws.write(row, 2, company)
        ws.write(row, 3, location)
        ws.write(row, 4, newLink)
        ws.write(row, 5, datetime.now(), dateStyle)
        ws.write(row, 6, 'Not Applied', appliedStyle)

        row+=1

    wb.save('jobs.xls')