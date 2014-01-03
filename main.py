'''
Most comments are in-line, but at a high level this takes a number of inputs
(first name, last name, nickname, middle initial, work email) and puts
together a lot of possible email addresses for them. Then it checks each of
them using the rapportive API to see if they exist, and tells you which ones
do.

Please don't use it for evil.
'''

from rapportive import rapportive


# this just takes an email and gets their user report from Rapportive
def getProfile(user):
  return rapportive.request(user)


# this checks if they have any results in Rapportive without breaking the query limit
def successCheck(user):
  while True:
    try:
      return rapportive.request(user).success
      break
    except AttributeError:
      return "No profile"


def possibleEmails(possible_name_combos, at_domain):
  return [item + '@' + at_domain for item in possible_name_combos]


# All of the basic possible email combinations from the data given. If you think of more then send a push request
def compileAllPossibleEmails(first_name, last_name, middle_initial, nick_name, at_domain, try_gmail):
  possible_name_combos = []
  possible_emails      = []
  possible_gmails      = []
  first_initial        = first_name[:1]
  last_initial         = last_name[:1]

  if first_name != "" and last_name != "":
    possible_name_combos.append(first_name + "." + last_name)
    possible_name_combos.append(first_name + "." + last_initial)
    possible_name_combos.append(first_name)
    possible_name_combos.append(first_name + last_name)
    possible_name_combos.append(first_name + last_initial)
    possible_name_combos.append(first_initial + "." + last_name)
    possible_name_combos.append(first_initial + last_name)
    possible_name_combos.append(last_name + "." + first_name)
    possible_name_combos.append(last_name + "." + first_initial)
    possible_name_combos.append(last_name)
    possible_name_combos.append(last_name + first_name)
    possible_name_combos.append(last_name + first_initial)
  if first_name != "" and last_name != "" and middle_initial != "":
    possible_name_combos.append(first_name + "." + middle_initial + "." + last_name)
    possible_name_combos.append(first_name + "." + middle_initial + "." + last_initial)
    possible_name_combos.append(first_name + middle_initial + last_name)
    possible_name_combos.append(first_name + middle_initial + last_initial)
    possible_name_combos.append(first_initial + "." + middle_initial + "." + last_name)
    possible_name_combos.append(first_initial + middle_initial + last_name)
  if nick_name != "" and last_name != "" and middle_initial != "":
    possible_name_combos.append(nick_name + middle_initial + last_name)
    possible_name_combos.append(nick_name + "." + middle_initial + "." + last_name)
  if nick_name != "" and first_name != "":
    possible_name_combos.append(first_name + "." + nick_name)
    possible_name_combos.append(first_name + nick_name)
    possible_name_combos.append(nick_name + "." + first_name)
    possible_name_combos.append(nick_name + first_name)
  if nick_name != "" and last_name != "":
    possible_name_combos.append(last_name + "." + nick_name)
    possible_name_combos.append(last_name + nick_name)
    possible_name_combos.append(nick_name + "." + last_name)
    possible_name_combos.append(nick_name + last_name)

  if at_domain != '':
    possible_emails = possibleEmails(possible_name_combos, at_domain)

  if try_gmail == 'y':
    possible_gmails = possibleEmails(possible_name_combos, 'gmail.com')

  return possible_emails + possible_gmails


# creates a set of the real emails based on success-checking each of the possible ones
def findEmail(emails):
  realEmails = []
  for i in emails:
    if successCheck(i) == "No profile":
      pass
    else:
      realEmails.append(i)
  return realEmails


# prints out the real emails
def results(email):
  if email != [] and len(email) == 1:
    print "Here's their email address! " + str(email)
  elif email == []:
    print "Sorry I didn't find anything =("
  elif len(email) > 1:
    print "I found a few possibilities..."
    print email


# runs the program with the appropriate user inputs
def main():
  print "If you don't have any of this information, just leave it blank and it will be skipped. I'd recommend trying to get their work email if possible though"
  results(findEmail(compileAllPossibleEmails(raw_input("First name: "), raw_input("Last name: "), raw_input("Middle initial: "), raw_input("Nickname: "), raw_input("Email Domain in format of 'xyz.com': "), raw_input("Should we try gmail? (y/n): "))))


if __name__ == "__main__":
  main()
