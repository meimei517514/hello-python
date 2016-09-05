with open("textsample.txt") as file:
	if file:
		for i in file.readlines():
			print i,"word count:",len(i)
			
