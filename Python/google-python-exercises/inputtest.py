import sys

def Hello(name):
	if name == 'Alice' or name == 'Nick':
		print 'Alert: Alice Mode'
		name = name + '????'
	else:
		print 'Else'
	name = name + '!!!!'
	print 'Hello', name

# Define a main() function
def main():
	Hello(sys.argv[0])

# Standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()