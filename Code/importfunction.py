#import the process funtion and some other modules
from openafm_function import gwybas
import sys
import os
import pprint

#define the rootdir that needs to be processed, all subdirs will also be processed!
rootdir = r'C:\Users\basst\Documents\AFM Scans (raw + treated)'
filepaths=[]
subpaths=[]
filenames=[]

#list of extentions that need to be checked for, might be a nicer way to do this.
list=['.000','.001','.002','.003','.004','.005','.006','.006','.007','.008','.009','.010','.011','.012','.013','.014']

#walk through all files in the rootdir and its subdirs and list the AFM files (.00? files)
for subdir, dirs, files in os.walk(rootdir):
	# print files
    for file in files:
    		if os.path.splitext(file)[1] in list:
    			filepaths.append(os.path.join(subdir, file))
    			subpaths.append(os.path.join(subdir))
    			filenames.append(os.path.join(file))

#constant to count how many graphs were created
existed=0
created=0
# print(len(filepaths))
# print(filepaths[308])
# pprint.pprint(filepaths)
#iterate over all the AFM files
for i in range(0,len(filenames)):
	# print(i)
	#check of a .gwy file already exists
	if os.path.isfile(filepaths[i]+'.gwy') is False:
		#run the process over files that don't have a .gwy (and implied .jpg) yet	
		gwybas(filepaths[i])
		# print(filepaths[i])
		#print the location/filename of the created graph, relative to the rootdir
		print subpaths[i][len(rootdir):]+'\\'+filenames[i]+'.gwy',' and .jpg are created'
		created+=1
	elif os.path.isfile(filepaths[i]+'.gwy') is True:
		#do nothing if a .gwy (and implied .jpg) already exist
		# print subpaths[i][len(rootdir):]+'\\'+filenames[i]+'.gwy', ' already exists'
		existed+=1
	else:
		#exception if something weird is going on
		print('something wrong')

#print how many new graphs were created and how many already existed
print existed,'graphs already existed,',created,'additional ones were created.'