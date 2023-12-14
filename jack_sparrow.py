input_string = input('Enter the values of A B C D separated by space \n')
user_list = input_string.split()

n_boats = 1;
for i in range(len(user_list)):
  user_list[i] = int(user_list[i])
  n_boats = n_boats + (user_list[i] * (i + 0))

print("Number of boats = ", n_boats)
