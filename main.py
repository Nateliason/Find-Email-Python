'''
Most comments are inline, but at a high level this takes a number of inputs (first name, last name, nickname, middle initial, work email) and puts together a lot of possible email addresses for them. Then it checks each of them using the rapportive API to see if they exist, and tells you which ones do.

Please don't use it for evil.
'''

from rapportive import rapportive

def getProfile(user): #this just takes an email and gets their user report from Rapportive
	return rapportive.request(user)
	
def successCheck(user): #this checks if they have any results in Rapportive without breaking the query limit
	while True:
		try:
			return rapportive.request(user).success
			break
		except AttributeError:
			return "No profile"
			
			
def possibleEmails(first, last, middle, nickname, workemail, gmail): #All of the basic possible email combinations from the data given. If you think of more then send a push request
	possibles = []
	if first != "" and last != "" and gmail == "y":
		possibles.append(first + last + "@gmail.com")
		possibles.append(last + first + "@gmail.com")
		possibles.append(first[:1] + last + "@gmail.com")
		possibles.append(first + last[:1] + "@gmail.com")
		possibles.append(last + first[:1] + "@gmail.com")
		possibles.append(first + "." + last + "@gmail.com")
		possibles.append(last +  "." + first + "@gmail.com")
		possibles.append(first[:1] + "." + last + "@gmail.com")
		possibles.append(first + "." + last[:1] + "@gmail.com")
		possibles.append(last + "." + first[:1] + "@gmail.com")
	if first != "" and last != "" and middle != "" and gmail == "y":
		possibles.append(first + middle + last + "@gmail.com")
		possibles.append(first[:1] + middle + last + "@gmail.com")
		possibles.append(first + middle + last[:1] + "@gmail.com")
		possibles.append(first + "." + middle + "." + last + "@gmail.com")
		possibles.append(first[:1] + "." + middle + "." + last + "@gmail.com")
		possibles.append(first + "." + middle + "." + last[:1] + "@gmail.com")
	if nickname != "" and last != "" and gmail == "y":
		possibles.append(nickname + last + "@gmail.com")
		possibles.append(last + nickname + "@gmail.com")
		possibles.append(nickname + "." + last + "@gmail.com")
		possibles.append(last + "." + nickname + "@gmail.com")
	if nickname != "" and last != "" and middle != "" and gmail == "y":
		possibles.append(nickname + middle + last + "@gmail.com")
		possibles.append(nickname + "." + middle + "." + last + "@gmail.com")
	if first != "" and last != "" and workemail != "":
		possibles.append(first + workemail)
		possibles.append(last + workemail)
		possibles.append(first + last + workemail)
		possibles.append(last + first + workemail)
		possibles.append(first[:1] + last + workemail)
		possibles.append(first + last[:1] + workemail)
		possibles.append(last + first[:1] + workemail)
		possibles.append(first + "." + last + workemail)
		possibles.append(last + "." + first + workemail)
		possibles.append(first[:1] + "." + last + workemail)
		possibles.append(first + "." + last[:1] + workemail)
		possibles.append(last + "." + first[:1] + workemail)
	if nickname != "" and last != "" and workemail != "":
		possibles.append(nickname + last + workemail)
		possibles.append(nickname + first + workemail)
		possibles.append(nickname + "." + last + workemail)
		possibles.append(nickname + "." + first + workemail)

	return possibles
		
			
def findEmail(emails): #creates a set of the real emails based on success-checking each of the possible ones 
	realEmails = []
	for i in emails:
		if successCheck(i) == "No profile":
			pass
		else:
			realEmails.append(i)
	return realEmails
			

def results(email): #prints out the real emails
	if email != [] and len(email) == 1:
		print "Here's their email address! " + str(email)
	elif email == []:
		print "Sorry I didn't find anything =("
	elif len(email) > 1:
		print "I found a few possibilities..."
		print email
			
			
def main(): #runs the program with the appropriate user inputs
	print "If you don't have any of this information, just leave it blank and it will be skipped. I'd recommend trying to get their work email if possible though"
	results(findEmail(possibleEmails(raw_input("First name: "), raw_input("Last name: "), raw_input("Middle initial: "), raw_input("Nickname: "), raw_input("work email in the format '@xyz.com': "), raw_input("Should I try gmail as well? (y/n): "))))
	
	
if __name__ == "__main__":
	main()

