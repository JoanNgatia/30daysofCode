# Instructions
# Given the meal price (base cost of a meal),
# tip percent (the percentage of the meal price being added as tip),
# and tax percent for a meal,
# find and print the meal's total cost.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tipPercent = mealCost * tipPercent / 100
taxPercent = mealCost * taxPercent / 100
totalCost = mealCost + tipPercent + taxPercent
totalCost = math.round(totalCost)
print "The total meal cost is %d dollars." % totalCost
