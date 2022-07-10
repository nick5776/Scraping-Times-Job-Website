from bs4 import BeautifulSoup
import requests

print('Skills you are familiar with')
familiar_skill = input('>')
print(f"Showing results on the basis of your skill {familiar_skill}")

link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(link, 'lxml')
jobs = soup.find('li', class_ = "clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date = job.find('span', class_ = 'sim_posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if familiar_skill in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More Info: {more_info}")

            print('')






