costPrice = float(input("ENTER THE COST PRICE OF THE PRODUCT: "))
sellPrice = float(input("ENTER THE SELL PRICE OF THE PRODUCT: "))
profit = sellPrice - costPrice
newSellingPrice = 1.05 * profit + costPrice
print("The profit is", profit)
print("To increse profit by 5% the selling should be", newSellingPrice)
