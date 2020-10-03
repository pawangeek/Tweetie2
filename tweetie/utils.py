from datetime import datetime ,timedelta
import requests, time
from urllib.parse import urlparse


def sevenspan():
    return datetime.today() - timedelta(days=7)

def getlinks(myurl):

	try:
	    r = requests.get(parsed_uri) 
	    finaldest = r.url

	    time.sleep(0.1)

	    dom = urlparse(finaldest)
	    domain = '{uri.netloc}/'.format(uri=dom)

	except:
		finaldest = "http://www.example.com"
		domain = "example.com"

    return finaldest, domain