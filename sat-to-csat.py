import sys

# Open file and split input into list
input = sys.argv[1]
content = input.split("c")
n = len(content)

# Nodes
output = input + "X"

# OR gates
for i in range(0,n):
    output += content[i] + "e" + "OR" + str(int(i / 3) + 1) + "c"
output = output[:-1] + "X"

# AND gate
for i in range(0, int(n/3)):
    output+= "OR" + str(i+1) + "e" + "AND" + "c"
output = output[:-1]

# Print output
print(output)
