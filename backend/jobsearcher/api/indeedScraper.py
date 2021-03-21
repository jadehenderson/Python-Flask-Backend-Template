import requests
from bs4 import BeautifulSoup

## This file is the Indeed.com scraper for the Backend PackHacks workshop. This file is set
## up in a extract, transform, and return format, which should be followed for other similar
## scrappers if you are wanting to scrape other sites.
## We import requests and BeautifulSoup from pip install beautifulsoup4 to do the scrapping.
## @author Travis Walter - 3/16/2021

## This extract function extracts the html webpage from the url we are giving it and returning
## it to the caller (using request and BeautifulSoup). This function needs one parameter that
## I haven't added in this template. This will return an instance of BeautifulSoup, which I
## haven't added in this template.
def extract(pageNum):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=Software+Engineer&l=Raleigh%2C+NC&radius=50&start={pageNum}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

## This transform function pulls the information from the html content extracted by the extract
## function. We pull all the information we want from the html here and add a job dictionary to
## a joblist list. This function needs two paramters that I haven't added in this template.
## This will return one of the edited parameters we pass in, which I haven't added in this
## template.
def transform(jobList, soup):

    allDivs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')

    for item in allDivs: 
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
            except:
                salary = ''

        summary = item.find('div', class_ = 'summary').text.strip().replace('\n', '')

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }

        jobList.append(job)

    return jobList

## This getList function is the frontfacing function for this file. This function is called
## by the Flask endpoint to get the full list of job dictionaries. This will return a list of
## jobs, which I haven't implemented in this template.
def getList():

    jobList = []

    for i in range(0, 50, 10): 
        content = extract(i)
        transform(jobList, content)
    return jobList