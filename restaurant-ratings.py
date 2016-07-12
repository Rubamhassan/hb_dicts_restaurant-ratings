score = {}  
input_file = open("scores.txt")
for line in input_file:
    line = line.rstrip()
    line = line.split(":")
    score[line[0]]=line[1] 

restaurant_list = score.items()
restaurant_list.sort()

for item in restaurant_list:
    print "%s is rated at %s" % (item[0], item[1]) 




# create a list of keys
# sort the keys
# for each key in the sorted keys:
#     print the restaurant name and score# your code goes here
