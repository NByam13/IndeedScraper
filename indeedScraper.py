import sys
import requests
from bs4 import BeautifulSoup

url = ''

#First we need to gather command line arguments, if there are none we're going to end the script
if len(sys.argv) == 1:
	print('Please specify which site to search and what keywords to search for.') #don't really like this, maybe ask for their preferred keywords
	exit(0)
	
elif len(sys.argv) == 2 and sys.argv[1].startswith('-url'): # if a site is used as an arg, decide if it is indeed or monster
	if sys.argv[1].find('indeed') != -1 :
		url = 'https://ca.indeed.com/jobs?'
	elif sys.argv[1].find('monster') != -1:
		url = 'https://www.monster.ca/jobs/search/?'
	else:
		print('That job search website is currently unsupported. Please use either Indeed or Monster')
		# get either indeed or monster
	
# get the data from the url in the form of html sent after a request to their server
url = 'https://ca.indeed.com/jobs?q=software developer&l=Waterloo,ON&radius=25'
page = requests.get(url)

# Create a soup object of the html that we can parse through to find what I want
indeedSoup = BeautifulSoup(page.content, 'html.parser')

# Create an iterable called job postings that has all the html data from indeed pertaining to their clickable cards.
searchResult = indeedSoup.find(id= 'resultsCol')

jobPostings = searchResult.find_all('div', class_='jobsearch-SerpJobCard')

print('\n')

# Iterate through the jobPostings variable and cherry pick information, such as job title, company, location, post date
for job in jobPostings:

	jobTitle = job.find('h2', class_='title')
	jobCompany = job.find('span', class_='company')
	jobLocation = job.find('span', class_='location')
	if jobLocation == None:
		jobLocation = job.find('div', class_='location')
	jobDate = job.find('span', class_='date')

	print(jobTitle.text.strip())
	print(jobCompany.text.strip())
	print(jobLocation.text.strip())
	print(jobDate.text.strip())
	print('\n')

