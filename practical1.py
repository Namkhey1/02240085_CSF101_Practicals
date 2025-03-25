# Question 1

first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inverse_list = []


while len(first_list) > 0:
    temp = first_list.pop()
    inverse_list.append(temp)

print(inverse_list)


# Question 2

def reverse_array(first_list):
    inverse_list = []

    while len(first_list) > 0:
        temp = first_list.pop()
        inverse_list.append(temp)

    return inverse_list

first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inverse_list = reverse_array(first_list)
print(inverse_list)