
from bitarray import bitarray
import mmh3

read_input = dict()
input_set = []
tn = int(0)
fp = int(0)

# reading the file which has S
lines1 = open("listed_username_30.txt", "r", encoding='ISO-8859-1')
for line in lines1:
	read_input[line] = line
	input_set.append(line)
lines1.close()

# set the parameters
n = len(input_set)
m = 4 * n
bit_vector = bitarray(m)
bit_vector.setall(bool(0))

# mapping S to bit_vector
for i in input_set:
	h1 = mmh3.hash(i,23) % m
	h2 = mmh3.hash(i,29) % m
	h3 = mmh3.hash(i,31) % m
	bit_vector[h1] = bool(1)
	bit_vector[h2] = bool(1)
	bit_vector[h3] = bool(1)
	 
# reading the stream
lines2 = open("listed_username_365.txt", "r",encoding='ISO-8859-1')
for line in lines2:
	h1 = mmh3.hash(line, 23) % m
	h2 = mmh3.hash(line, 29) % m
	h3 = mmh3.hash(line, 31) % m
	if (bit_vector[h1] is bool(1)) and (bit_vector[h2] is bool(1)) and (bit_vector[h3] is bool(1)):
		if line not in read_input:
			fp = fp + 1
	else:
		tn = tn + 1
lines2.close()

# printing FP
print ((float(fp)/(fp + tn)) * 100, "%")


	




































