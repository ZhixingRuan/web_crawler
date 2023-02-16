import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
a web crawler for get the routes name and grade from mountain project
'''


req = requests.get('https://www.mountainproject.com/area/classics/105744270/carter-lake')
webpage = req.text
soup = BeautifulSoup(webpage, 'html.parser')

name = soup.find_all('strong')
name = name[1:]
grade = soup.find_all('span', attrs={"class":'rateYDS'})

data = {"problem_name":[], "grade":[]}
for n in name:
    data["problem_name"].append(n.get_text())
for v in grade:
    data['grade'].append(v.get_text())

df = pd.DataFrame(data)
df.to_csv('carter_lake_classic_problems.csv')
