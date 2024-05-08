temp_input = input("Please enter a word: ")
temp_type = temp_input[-1::]
temp = float(temp_input[:-1])

if temp_type == 'F' or temp_type == 'f':
    new_temp = (((5*temp)-160)/9)
    new_type = 'C'
elif temp_type == 'C' or temp_type == 'c':
    new_temp = (((9*temp)+160)/5)
    new_type = 'F'

new_temp = (str(new_temp) + new_type)
print(new_temp)