print(f"""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: ${202+118+2250+1680+1075+80}""")
print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())
net_income = 5405 - staff_expenses - other_expenses
print("Net income: $ " + str(net_income))