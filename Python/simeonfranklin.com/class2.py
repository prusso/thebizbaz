names = ['John', 'Luke', 'Paul', 'Mark', 'Richard', 'Christopher', 'Dan', 'Sam']

# Print all names in the list
for name in names:
	print "Hello " + name

# Print last name
print "Hello " + names[-1]

# Print last two names
for name in names[6:]:
	print "Hello " + name

# Print every other name
for name in names[::2]:
	print "Hello " + name

# Reverse
rev = names[:]
rev.reverse()
print rev

# Alphabetical
alpha = names[:]
alpha.sort()
print alpha