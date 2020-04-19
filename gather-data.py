import datetime
import json
import requests
from bs4 import BeautifulSoup

# Keno.de only shows the last 30 draws

data = {}
today = datetime.date.today()
kenoUrl = "https://www.lottozahlenonline.com/keno/archiv/{}/{}"
maxYear = 2004
maxMonth = 2

def extractNumbers(yr, mo):
  page = BeautifulSoup(requests.get(kenoUrl.format(yr, mo)).content, 'html.parser')

  rawNumbers = []
  rawPlus5s = []

  # Numbers
  numberElements = page.find_all('p')
  for element in numberElements:
    if element.text.startswith('In der '):
      numbers = element.text.split(' ')[19:-1]
      rawNumbers.append(numbers)

  # Plus5
  plusElements = page.find_all('strong')
  for element in plusElements:
    if element.text.startswith('Plus5: '):
      numbers = element.text.split(' ')[1]
      numbers = [char for char in numbers]
      rawPlus5s.append(numbers)
  
  # Sort and Insert
  rawNumbers = list(reversed(rawNumbers))
  rawPlus5s = list(reversed(rawPlus5s))

  for d in range(len(rawNumbers)):
    if str(yr) not in data:
      data[str(yr)] = {}
    if str(mo) not in data[str(yr)]:
      data[str(yr)][str(mo)] = {}
    if str(d+1) not in data[str(yr)][str(mo)]:
      data[str(yr)][str(mo)][str(d+1)] = {}
    data[str(yr)][str(mo)][str(d+1)]["numbers"] = rawNumbers[d]
    data[str(yr)][str(mo)][str(d+1)]["plus5"] = rawPlus5s[d]
  
  print("Done:", yr, mo)

for yr in range(maxYear, today.year + 1):
  startMonth = 1
  if yr == maxYear:
    startMonth = maxMonth

  for mo in range(startMonth, 12 + 1):
    extractNumbers(yr, mo)
  

with open('data/data.json', 'w') as f:
  f.write(json.dumps(data))
print("Data extracted!")
