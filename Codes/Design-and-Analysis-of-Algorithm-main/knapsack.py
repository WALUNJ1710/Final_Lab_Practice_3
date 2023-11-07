class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):

	# Sorting Item on basis of ratio
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 

	# Result(value in Knapsack)
	finalvalue = 0.0

	# Looping through all Items
	for item in arr:

		# If adding Item won't overflow, 
		# add it completely
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.profit

		# If we can't add current Item, 
		# add fractional part of it
		else:
			finalvalue += item.profit * W / item.weight
			break
	
	# Returning final value
	return finalvalue



W = int(input("Enter the weight capacity :"))
num_items = int(input("Enter the number of items: "))
items = []
for i in range(num_items):
    profit, weight = map(int, input(f"Enter the profit and weight for item {i + 1}: ").split())
    items.append(Item(profit, weight))
max_val = fractionalKnapsack(W, items)
print(max_val)

 