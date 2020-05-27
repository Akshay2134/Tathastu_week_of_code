Cost_price= float(input("Enter the cost price of the product: "))
Selling_price= float(input("Enter the selling price of the product: "))
profit= Selling_price - Cost_price
New_Selling_Price= 1.05 * profit + Cost_price
print("The profit from this sell is", profit)
print("To increase the profit by 5% the selling price should be", New_Selling_Price)
