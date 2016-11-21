# For all active legislators in MO -- http://openstates.org/api/v1/legislators/?state=mo&chamber=upper&active=true
# For all bills introduced to MO Senate in 2016 -- http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016
# For list of legislation just related to guns -- http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&q=Guns

import json
import requests

url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&q=Guns'

r = requests.get(url)

response_data = r.content

data = json.loads(response_data)

http = 'http://openstates.org/api/v1/bills/?state=mo&q=Guns'

outcome = requests.get(http)
response = r.content

for result in data:
	print result['bill_id']
	print result['title']
	print result['session']
	print outcome
	for outcome in result:
		if ('actions' == ''):
			print outcome['last']
	print result['subject']
	print result['actions']
	print '----------------'