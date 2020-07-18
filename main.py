import requests

URL='https://www.monster.ca/jobs/search/?q=Software-Engineer-intern&where=Toronto__2C-Canada-&jobid=b697209f-417b-4e67-8ac5-e19487dc85b0'
# URL='https://ca.indeed.com/jobs?q=software%20engineer%20intern&l=Toronto%2C%20ON&vjk=4fb9ee159ff25c91'
page=requests.get(URL)

print(page.content)
