import json
import urllib2

data = {
	  'basics': {
	    'name': 'Peter Podniesinski',
	    'label': 'Mr',
	    'email': 'peterpod@hotmail.com',
	    'phone': '6319464436',
	    'about': 'I am a Junior Information Systems major at Carnegie Mellon. I am looking for a software engineering position specifically in web application development. I have skills in different front end frameworks like rails and PHP and for the backend I know MySQL, Postgre',
	    'location': {
	      'address': '12 Kensett Lane',
	      'zip': '06820',
	      'city': 'Darien',
	      'countryCode': 'US',
	      'state': 'CT'
	    }
	  },
	  'work': [{
	    'company': 'Tradeweb',
	    'position': 'Application Developer',
	    'startDate': '06/1/2014',
	    'endDate': '08/14/2014',
	  }],
	  'education': [{
	    'institution': 'Carnegie Mellon University',
	    'major': 'Information Systems',
	    'graduationdate':'2016',
	    'gpa': '3.48',
	  }],
	  'skills': ['Ruby on Rails','Ruby','Python','PHP','SQL','Javascript','JQuery'],
	  'languages': ['English','Polish','Spanish'],
	  'urls': ['https://github.com/peterpod']
}

url= 'http://nextjump-careers.com/apply'
req = urllib2.Request('http://nextjump-careers.com/apply')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))