import os


file_dir = os.path.dirname(__file__)
with open(file=os.path.join(file_dir, "input.txt")) as file:
    binary_list = file.readlines()

binary_str_length = len(binary_list[1]) - 1
binary_list_length = len(binary_list)

zero_count = 0
value_gamma = []
value_epsilon = []
gamma_rate_binary = ""
epsilon_rate_binary = ""


for x in range(0, binary_str_length):
    for y in binary_list:
        if y[x] == "0":
            zero_count += 1
    if zero_count > len(binary_list) / 2:
        value_gamma.append("0")
        value_epsilon.append("1")
    else:
        value_gamma.append("1")
        value_epsilon.append("0")
    zero_count = 0

gamma_rate_binary = gamma_rate_binary.join(value_gamma)
gamma_rate = int(gamma_rate_binary, 2)

epsilon_rate_binary = epsilon_rate_binary.join(value_epsilon)
epsilon_rate = int(epsilon_rate_binary, 2)

power = gamma_rate * epsilon_rate
print(power)
