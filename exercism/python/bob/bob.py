"""
bob.py

Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him.
He says 'Fine. Be that way!' if you address him without saying anything.
He answers 'Whatever.' to anything else.
"""


def hey(what):

	what = what.strip()
	
	if what == '':
		return 'Fine. Be that way!'

	elif what.isupper():
		return 'Whoa, chill out!'

	elif what.endswith('?'):
		return "Sure."

	else:
		return 'Whatever.'