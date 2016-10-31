import urllib.request

def read_text():

	text = open('/Users/Leo/python_drills/profane.txt')
	contents = text.read()
	print(contents)
	text.close()
	check_profanity(contents)

def check_profanity(text_to_check):

	with urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check) as response:
		output = response.read
		print(output)

read_text()