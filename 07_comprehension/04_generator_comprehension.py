# Generator: (expression for item in itearable if condition)

sale_price=[5,15,10,8,9,6,3]

prices=(sales for sales in sale_price if sales>5)
print(prices)

prices= sum(sales for sales in sale_price if sales>5)
print(prices)