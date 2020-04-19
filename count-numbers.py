import json
import random

def testNumbers():
  zahlen = []
  while len(zahlen) is not 20:
    r = random.randint(1, 70)
    if r not in zahlen:
      zahlen.append(r)
  return sorted(zahlen)

f = open('data/data.json', 'r').read()
data = json.loads(f)

numbers = {}
testData = {}
plus5 = {}

for year in data:
  for month in data[year]:
    for day in data[year][month]:
      currentDay = data[year][month][day]

      for n in currentDay['numbers']:
        if str(n) not in numbers:
          numbers[str(n)] = 0
        numbers[str(n)] += 1

      for n in testNumbers():
        if str(n) not in testData:
          testData[str(n)] = 0
        testData[str(n)] += 1

      for n in currentDay['plus5']:
        if str(n) not in plus5:
          plus5[str(n)] = 0
        plus5[str(n)] += 1

# Write to CSV

csvNumbers = ''
for i in numbers:
  csvNumbers += '{},{}\r'.format(i, numbers[i])
with open('data/count-numbers.csv', 'w') as f:
  f.write(csvNumbers)

csvTestNumbers = ''
for i in testData:
  csvTestNumbers += '{},{}\r'.format(i, testData[i])
with open('data/count-numbers-test.csv', 'w') as f:
  f.write(csvTestNumbers)

csvPlus5 = ''
for i in plus5:
  csvPlus5 += '{},{}\r'.format(i, plus5[i])
with open('data/count-plus5.csv', 'w') as f:
  f.write(csvPlus5)
