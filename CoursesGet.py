import requests
from bs4 import BeautifulSoup

url = 'https://guide.wisc.edu'

# https://guide.wisc.edu/search/?search=COMP+SCI+200

# Generate one search url
def GenerateSearchUrl(url, searchTarget):
    targetUrl = url + '/search/?search='
    targetUrl += searchTarget.replace(' ', '+')

    return targetUrl

# Search one course and get its info
def SearchOnePage(coreUrl, url):
    # Url get
    response = requests.get(url)
    responseHtml = response.text

    # Process with beautiful soup
    soup = BeautifulSoup(responseHtml, 'lxml')
    # print(soup)

    # Search results
    results = soup.find_all('div', {'class': 'searchresult'})
    print(results)
    result = results[0]
    
    # Searched course
    courseResult = result.find('div', {'class': 'courseblock'})
    
    # Course Info
    courseCredit = courseResult.find('p', {'class': 'courseblockcredits'}).get_text()
    courseDiscription = courseResult.find('p', {'class': 'courseblockdesc noindent'}).get_text()
    courseDatas = courseResult.find_all('p', {'class': 'courseblockextra noindent clearfix'})
    preresuisite = courseDatas[0].find('span', {'class': 'cbextra-data'})
    preresuisiteCourseUrls = preresuisite.find_all('a', {'class': 'bubblelink code'})
    
    preresuisiteCourses = []

    for preresuisiteCourseUrl in preresuisiteCourseUrls:
        preresuisiteCourses.append(preresuisiteCourseUrl.get_text() + ':' + coreUrl + preresuisiteCourseUrl['href'])

    preresuisiteCoursesNames = []
    for preresuisiteCourseUrl in preresuisiteCourseUrls:
        preresuisiteCoursesNames.append(preresuisiteCourseUrl.get_text())

    return [courseCredit, courseDiscription, preresuisite.get_text(), preresuisiteCourses, preresuisiteCoursesNames]

# print (SearchOnePage('https://guide.wisc.edu/search/?search=MATH+141', url))