cost_price = float(input("Enter the Cost Price : "))
selling_price = float(input("Enter the Selling Price : "))
profit = 0
if selling_price > cost_price : 
    profit = selling_price - cost_price

print(" The profit =",profit)

new_sell_price = selling_price + (0.05*cost_price)

print("New selling price for which the profit will increase by 5% =",new_sell_price)
