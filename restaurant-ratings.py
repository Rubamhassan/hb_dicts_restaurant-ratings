score = {}  
input_file = open("scores.txt")
for line in input_file:
    line = line.rstrip()
    line = line.split(":")
    score[line[0]]=line[1] 

for item in score:
    "%s is rated at %d" % item, score[item] 




# create a list of keys
# sort the keys
# for each key in the sorted keys:
#     print the restaurant name and score# your code goes here
