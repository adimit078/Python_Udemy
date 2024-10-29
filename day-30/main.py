# #FileNotFound
#
# with open("filename.txt") as file:
#     lines = file.readlines()
#

try:
    file = open("new_file.txt")
except FileNotFoundError:
    file = open("new_file.txt", "w")



# #KeyError
# a_dictionary = {"Key":"value"}
# a_dictionary["newKey"]


