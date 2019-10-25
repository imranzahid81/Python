import re

# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print "You failed to match %s" % (email)
        elif not your_pattern:
            print "Forgot to enter a pattern!"
        else:
            print "Pass"


# Your pattern here!
pattern = r"[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
test_email(pattern)


# example 2 getting email input 

def email():
    email = raw_input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

    if match:
        print "valid email :::", match.group()
    else:
        print "not valid:::"

email()		# calling function
