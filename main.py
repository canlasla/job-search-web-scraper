import requests
from bs4 import BeautifulSoup

URL='https://www.monster.ca/jobs/search/?q=Software-Engineer-intern&where=Toronto__2C-Canada-&jobid=b697209f-417b-4e67-8ac5-e19487dc85b0'
# URL='https://ca.indeed.com/jobs?q=software%20engineer%20intern&l=Toronto%2C%20ON&vjk=4fb9ee159ff25c91'
page=requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
results=soup.find(id='ResultsContainer')
jobElements=results.find_all('section', class_='card-content')

for jE in jobElements:
    title_elem = jE.find('h2', class_='title')
    company_elem = jE.find('div', class_='company')
    location_elem = jE.find('div', class_='location')
    time_elem =jE.find('time')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print(time_elem)
    print()