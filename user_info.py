from rapportive import rapportive

def getProfile(user): #this just takes an email and gets their user report from Rapportive
	return rapportive.request(user)
	
print getProfile(raw_input())