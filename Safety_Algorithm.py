import sys
#check if parameters are passed, else take input
try:
	no = int(sys.argv[1])
except:
	no = eval(input("Enter number of processes: "));

#initilize list of 0 based no number of processes
process = [0 for i in range(no)]


#Check if parameters are passed, else take input
try:
	resource_no = int(sys.argv[2])
except:
	resource_no = eval(input("Enter number of resource types: "));


#Input total avaiable resources
total = []
available = []
for i in range(resource_no):
	val = eval(input("Enter total resource of type " + str(i) + ": "));
	total.append(val)
	available.append(val)


#initalize allocated
allocated = []
for i in range(no):
	inside = []
	for j in range(resource_no):
		val = eval(input("Enter allocated " + str(j) + " for process " + str(i) + ": "));
		#check if input doesnt exceed the available
		if val <= available[j]:
			available[j] -= val
			inside.append(val);
		else:
			raise ValueError("Invalid Inputs")
	allocated.append(inside);

#initialize max resources requires per process

max = []
for i in range(no):
	inside = []
	for j in range(resource_no):
		val = eval(input("enter max resource " + str(j) + " for process " + str(i) + ": "));
		#check if max resource required doesn't exceed  total resources
		if val <= total[j]:
			inside.append(val)
		else:
			raise ValueError("Invalid Inputs. Maximum required exceeded available")
	max.append(inside)
print(process)


#calculate need
need = []
for i in range(len(process)):
	inside = []
	for j in range(len(max[0])):
		val = max[i][j] - allocated[i][j];
		inside.append(val);
	need.append(inside);


print("allocated", allocated)
print("Max", max)
print("Need", need)
print("Total", total)
safety_sequence = []
while True:
	#Set completed (flag) set to false as no completed process in the current loop
	completed = False;
	for i in range(len(process)):
		#Check if current process is completed
		if process[i] == 0:
			#Set flag to True to indicate if all of the resource type needs are less then available per process
			flag = True;
			for j in range(len(max[i])):
				#if need is greater than available then set flag to false
				if need[i][j] > available[j]:
					flag = False;
			#if all need is < available then set process to completed
			if flag:
				completed = True
				#Append current process to safety sequence list
				s = "P" + str(i)
				safety_sequence.append(s);
				process[i] = 1;
				#Increment available resource
				for k in range(len(max[i])):
					available[k] += allocated[i][k];
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
