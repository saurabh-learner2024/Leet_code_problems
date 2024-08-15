def splitting_list_into_variables(color):
    var1, var2, var3 = color
    return var1, var2, var3


color = [
    ("Black", "#000000", "rgb(0, 0, 0)"),
    ("Red", "#FF0000", "rgb(255, 0, 0)"),
    ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
]
variable_1, variable_2, variable_3 = splitting_list_into_variables(color)
print(variable_1)
print(variable_2)
print(variable_3)