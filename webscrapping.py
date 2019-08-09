import requests
from bs4 import BeautifulSoup
from csv import writer



response = requests.get('insert link to website or blog')

soup = BeautifulSoup(response.text, 'html.parser')

# the variable content is dynamic
#class here is to select only class element form the html
contents = soup.find_all(class_='short-content')

with open('contents.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['time', 'title']
    csv_writer.writerow(headers)

## for loop for looping through the blog post 
## looping only through the time a post was written and the title
    for content in contents:
        time = content.find(class_='content-time').get_text().replace('\n', '')
        title = content.find(class_='content-title').get_text().replace('\n', '')
        # print(time, title)

        #the posts are written to a csv file
        csv_writer.writerow([time, title])