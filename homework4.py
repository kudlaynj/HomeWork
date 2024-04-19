immutable_var = 24,25,26,27
immutable_var_1 = (24,25,26,27)
immutable_var_2 = tuple([24,25,26,27])
print(immutable_var)
print(immutable_var_1)
print(immutable_var_2)

mutable_list = ["tea", "coffee", "pepper"]
print(mutable_list)
mutable_list .extend("life")
print(mutable_list)
print("coffee" not in mutable_list)
mutable_list .remove("tea")
print(mutable_list)