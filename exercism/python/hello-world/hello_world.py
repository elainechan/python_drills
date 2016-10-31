#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if len(name) == 0:
        greeting = "Hello, World!"
        return greeting
    else:
        greeting = "Hello, " + name + "!"
        return greeting
