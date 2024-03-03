process = [0, 0, 0, 0, 0];
available = [3, 3, 2];
max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

need = []
for i in range(len(process)):
	inside = []
	for j in range(len(max[0])):
		val = max[i][j] - allocated[i][j];
		inside.append(val);
	need.append(inside);

p = eval(input("Enter process no for request"));
request = []
for i in range(len(available)):
	val = eval(input("Enter resource request instanse for type " + str(i) + ": "));
	if val > need[p][i] or val > available[i]:
		raise ValueError("Request can't be granted")
	else:
		request.append(val)


availablecopy = available.copy()
allocatedcopy = allocated.copy()

for i in range(len(allocatedcopy[0])):
	allocatedcopy[p][i] += request[i]
	availablecopy[i] -= request[i]

print("allocated", allocated)
print("max", max)
print("need", need)
safety_sequence = []
while True:
	#Set completed (flag) set to false as no completed process in the current loop
	completed = False;
	for i in range(len(process)):
		#Check if current process is completed
		if process[i] == 0:
			#Set flag to True to indicate if all of the resource type needs are less then available per process
			flag2 = True;
			for j in range(len(max[i])):
				#if need is greater than available then set flag to false
				if need[i][j] > availablecopy[j]:
					flag2 = False;
			#if all need is < available then set process to completed
			if flag2:
				completed = True
				#Append current process to safety sequence list
				s = "P" + str(i)
				safety_sequence.append(s);
				process[i] = 1;
				#Increment available resource
				for k in range(len(max[i])):
					availablecopy[k] += allocatedcopy[i][k];
			else:
				continue;
		else:
			continue;
	#If no process completed in one loop, system in deadlock.
	if completed == False:
		break

#if length of safety  sequence is equal to length of total processes then system is in safe state
if len(safety_sequence) == len(process):
	print("system is in safe state")
	print("Safety Sequence: ", safety_sequence)
else:
	print("system is in unsafe state")
