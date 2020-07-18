import requests
from bs4 import BeautifulSoup

URL='https://www.monster.ca/jobs/search/?q=Software-Engineer-intern&where=Toronto__2C-Canada-&jobid=b697209f-417b-4e67-8ac5-e19487dc85b0'
# URL='https://ca.indeed.com/jobs?q=software%20engineer%20intern&l=Toronto%2C%20ON&vjk=4fb9ee159ff25c91'
page=requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
results=soup.find(id='ResultsContainer')
jobElements=results.find_all('section', class_='card-content')

for elem in jobElements:
    linkElem = elem.find('a')
    titleElem = elem.find('h2', class_='title')
    companyElem= elem.find('div', class_='company')
    locationElem = elem.find('div', class_='location')
    timeElem =elem.find('time')

    if None in (linkElem, titleElem, companyElem, locationElem,timeElem):
        continue

    link=linkElem['href']
    print(titleElem.text.strip())
    print(companyElem.text.strip())
    print(locationElem.text.strip())
    print(timeElem.text.strip())
    print(f"Apply here: {link}\n")
    print()