# part 1
import re

# Read input from input.txt and save as string
with open("input.txt") as i:
    data = i.read()

# Split the string into a list of integers
data = re.split('[ |\n]', data)
i = 0
while i < len(data):
    if data[i] == '':
        data.pop(i)
    else:
        i += 1
data = [int(x) for x in data]

# Slice them in left and right column
left = data[::2]
right = data[1::2]

# Calculate the smallest distance between the  left and right column
left.sort()
right.sort()
distances = []
for i in range(len(left)):
    distances.append(abs(left[i] - right[i]))
# print("Distances: ", distances)    
    
# Print the sum of the distances
print("Sum of all distances: ", sum(distances))

# part 2
# Calculate a similarity score by counting how often a number of left appear in the right column 
# and multiply it by the count
score = []
for i in range(len(left)):
    score.append(left[i] * right.count(left[i]))
    
print("Score: ", sum(score))