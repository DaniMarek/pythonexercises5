# write a program that takes a list of strings 
# and a string containing a single character, 

# and prints a new list of all the strings containing that character 
# *Note: you may need more than one loop

def findChar():
	new_list=[]
	for i in range(0, len(word_list)):
		if word_list[i].find(char) !=-1:
			# for x in range(1,2):
			new_list.append(word_list[i])
	print 'new_list = '+ str(new_list)

# input
word_list = ['hello','world','my','name','is','Dani']
char = 'o'
findChar()