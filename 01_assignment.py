def helper(dictionary):
	"""
		This function will created dictionary map of every key and value of dictionary,
		 so that it can go through every integer which inter-connected.

	"""
	dictionary_map = {}
	for key, value in dictionary.items():
		if dictionary_map.get(key, None) == None:
			dictionary_map[key] = set({value}) # to stop duplication set is needed
		else:
			dictionary_map[key].add(value)

		if dictionary_map.get(value, None) == None:
			dictionary_map[value] = set({key})
		else:
			dictionary_map[value].add(key) 
	
	return dictionary_map


## Main Function Definition
def find_relation(dictionary, num):

	dictionary_map = helper(dictionary) #call helper function to create dict map
	print(dictionary_map)

	min_relation = float('inf')
	max_relation = float('-inf')

	visited_value = {num : True} # dict to keep track of visited value, otherwise a cycle well form.

	values_to_be_visited = []
	for i in dictionary_map[num]:
		values_to_be_visited.append(num) # list to keep the value needed to visit

	idx = 0

	# will loop over every non-visited but inter-connected values
	while idx < len(values_to_be_visited):
		current_value = values_to_be_visited[idx] # current integer visited

		
		if min_relation > current_value:
			min_relation = current_value
		elif max_relation < current_value:
			max_relation = current_value

		visited_value[current_value] = True

		# checking if value dosm't exist in visited dict then add that to non-visited list
		for i in dictionary_map[current_value]:
			if i not in visited_value:
				values_to_be_visited.append(i)

		idx+=1

	return max_relation, min_relation






####--------------------------------------#####


# initialization of max and min relation	
max_relation = 0
min_relation = 0

## dictionary in which relation is to be found
dictionary = {12:3, 4:26, 3:9, 9:6, 6:4, 11:19, 17:21}

if len(dictionary) > 0 and type(dictionary) == dict:
	num = input("Enter integer to find relation: ")

	if num.isnumeric():
		num = int(num)	
		if num in dictionary.keys() or num in dictionary.values():
			max_relation, min_relation = find_relation(dictionary, num) # main function is here
		else:
			print("Integer doesn't exist in dictionary, please enter valid integer.")
	else:
		print("Please enter valid interger to find the relation!")
else:
	print("PLease enter valid dictionary with integers!")



print("maximum relation: ", max_relation)
print("minimum relation: ", min_relation)