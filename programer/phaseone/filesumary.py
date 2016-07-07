import os,os.path

currfile = os.listdir(os.getcwd())

def sortfile(way):
	if way==1:
		newfile=map(lambda x:(x,os.stat(x).st_mode),currfile)
		newsortfile=sorted(newfile,key=lambda x:x[1])
		print newsortfile
		savefile=open("sortbyst_mode.txt","w")
		for i in newsortfile:
			savefile.write(str(i)+"\n")
		savefile.close()
	else:
		pass


sortfile(1)



