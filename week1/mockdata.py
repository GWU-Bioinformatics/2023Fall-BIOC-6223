import numpy as np
import json
import datetime 

mu, sigma = 150, 1

s = np.random.normal(mu, sigma, 100)
s = [ '%.2f' % elem for elem in s]

# for i in range(1,11):
# 	print ("April", str(i) + ",", "2015" + ",", s[i])

date = datetime.date(2015, 4, 1)
date_delta = datetime.timedelta(days = 1)

data = []

for i in s:
    data.append({'date': date.strftime('%B %d, %Y'), 'weight': i})
    date += date_delta

result = {'data': data}

json_result = json.dumps(result)

with open('./week1/kim.json', 'w') as f:
    f.write(json_result)