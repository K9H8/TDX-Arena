# opens the large jpg in binary. 

with open('img.jpg','rb') as file1:
	content = file1.read()


indexes = []
start = 0
marker =  b'\xff\xd8' #the marker for the beggining of img data.

# finds the indexes of marker.	
while True:
	index = content.find(marker, start)	
	if index != -1:
		indexes.append(index)
		start = index + 1
	else:
		break

# this loop goes through the indexes and saves the data in a seperate file.

for i in range(len(indexes)):
	if i != len(indexes)-1:
		with open(f"{i}.jpg",'wb') as file2:
			file2.write(content[indexes[i]:indexes[i+1]])
	else: 
		with open(f"{i}.jpg",'wb') as file2:
			file2.write(content[indexes[i]:])



