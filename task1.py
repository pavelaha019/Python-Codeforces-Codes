#Name : Pavel Ahammed 
#Id : 221074002

def reverse_middle(lst):
    if len(lst) <= 2:
        return lst
    result = []
    
    result.append(lst[0])
   
    for i in range(len(lst) - 2, 0, -1): 
        result.append(lst[i])
    return result
    
    result.append(lst[-1])

input_list = [1, 2, 3, 4, 5, 6, 7] 
output_list = reverse_middle(input_list) 
print(output_list)