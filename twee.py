import twython
from twython import Twython
import pymongo
from pymongo import Connection

akey = 'Ti2PbXfhvMNJGMXSQpQwbg'
se = 'kyv4UoxdgkPjYBPA03EgXaBWQB1AjYCgCdLMuhoDGNM'# these two are provided by our twitter app

twitter = Twython(akey, se, oauth_version=2) # we don't need to write, oauth_version 2 should ok
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython( akey, access_token=ACCESS_TOKEN)
connection = Connection() # connect to local mongo server
db = connection['test-twitter'] # connect to db called test-twitter
collection = db['iphone'] # the iphone collection (table)

N = 30 

a = twitter.search(q='iphone 5s', count = N) # search twitter about iphone 5s

for i in xrange(N):
	x = collection.find_one({'id': a['statuses'][i]['id']})
	if x:
		continue #this tweet is already in database
	else:
		pid = collection.insert( a['statuses'][i] ) #otherwise insert

print collection.find().count()

results = collection.find(limit = 100) # find the first 100 from our mongo db

f = open('iphoneresult.txt', 'w') # write them to test file

i = 0
for res in results:
	f.writelines( str(res) + '\n' )	
	f.writelines('\n')	

f.close()


'''
x = collection.find_one({'id': 386330477478420480L})

if x:
	print 'yes'
else:
	print 'no'

i = 0
for m in collection.find({'lang':'en'}): # these are about analysis
	if 'place' in m and m['place']:
		print m['place']
		print m['created_at']
		i += 1	
	#if 'user' in m:
	#	if 'location' in m['user'] and m['user']['location'] != '':
	#		print m['user']['location']
	#		i += 1
	#		print i

print i
'''




