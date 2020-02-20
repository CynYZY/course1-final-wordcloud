# Generate a new list containing the elements of list2
# Followed by the elements of list1 in reverse order
def combine_lists(list1, list2):
    list1.reverse()
    return list2 + list1

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))