def odd_elements(a_list):
    my_list = []
    for index in range(len(a_list)):
        if index % 2 != 0:
            my_list.append(a_list[index])
    return my_list

def combine(first_list, second_list):
    final_list = []
    for index in range(len(first_list)):
        final_list.append(first_list[index])
        final_list.append(second_list[index])
    return final_list
