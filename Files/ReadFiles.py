filename = "python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    print("#################################")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    print("#################################")
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
print("#################################")
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace("in Python you can","in your couch you cannot")
        print(line.rstrip())
print("#################################")
with open(filename,'a') as file_object:
    file_object.write("\ntu puedes lograr todo esto")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)