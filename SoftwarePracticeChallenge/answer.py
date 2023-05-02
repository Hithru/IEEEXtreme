inputs = []
with open("input.txt", "r") as file:
    for line in file:
        inputs.append(line.strip())

print(inputs)

directory_details = {"root": []}

directory_sizes = {"root": 0}

directory_parents = {"root": None}

current_directory = "root"
for line in range(1, len(inputs)):

    line_details = inputs[line].strip().split(" ")

    if len(line_details) == 3 and line_details[0] == "$":
        if line_details[2] == "..":
            if current_directory != "root":
                current_directory = directory_parents[current_directory]
        else:
            this_directory = line_details[2]
            if this_directory not in directory_parents:
                directory_parents[this_directory] = current_directory
                directory_details[this_directory] = []
                directory_sizes[this_directory] = 0
            current_directory = this_directory

    elif line_details[0] == "$":
        pass
        # it ls command
    elif line_details[0] == "dir":
        directory_details[current_directory].append(line_details[1])
        # directory details
    else:
        size = int(line_details[0])
        directory_details[current_directory].append(line_details[1])
        directory_sizes[current_directory] += size
        parent = directory_parents[current_directory]
        while parent != None:
            directory_sizes[parent] += size
            parent = directory_parents[parent]

            # file details
# print("Directory Details")
# print(directory_details)
#
# print("Directory Sizes")
# print(directory_sizes)

print("total_size", directory_sizes["root"])

total_sum = directory_sizes["root"]
size_needed_to_remove = total_sum - 40000000
remove_directory = "root"
remove_size = total_sum

total_sum_less = 0
for (key, value) in directory_sizes.items():
    if value <= 100000:
        total_sum_less += value
        # print(key)

    if value > size_needed_to_remove and value < remove_size:
        remove_size = value
        remove_directory = key

print(total_sum_less)
if size_needed_to_remove <= 0:
    print("No file needed to be removed")
else:
    print(remove_directory, remove_size)
