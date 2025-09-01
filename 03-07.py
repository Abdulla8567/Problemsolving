# Given the total seconds, compute and print equivalent hours, minutes, and seconds using arithmetic operations.

total_seconds = 8000
one_hour = 3600
hour = total_seconds // one_hour
remaining_sec = total_seconds % 60
min =  remaining_sec // 60
sec = remaining_sec % 60
print("Hours : ", hour)
print("Minutes : ",min)
print("Seconds : ",sec)

# Assign the price and quantity of two products. Calculate the total cost including 18% tax. Print a detailed bill.

price1 = 100
quantity1= 2
price2 = 150
quantity2 = 3
sub_total1 = price1 * quantity1
sub_total2 = price2 * quantity2
grand_total_before_tax = sub_total1 + sub_total2
tax = grand_total_before_tax * 0.18
total_cost = grand_total_before_tax + tax
print("-------Detailed Bill-------")
print("Total_cost_Before_Tax :",grand_total_before_tax)
print("Total_cost_after_tax :",total_cost)

#Compute the perimeter and area of a circle given a radius. Use the value of π from the math module.

radius = 2
perimeter_of_a_circle = 2 * 3.14 * radius
area_of_a_circle = 3.14 * radius * radius
print("perimeter_of_a_circle",perimeter_of_a_circle)
print("area_of_a_circle",area_of_a_circle)

# Given a temperature in Celsius, convert it to Fahrenheit using the formula and print both values.(F = C × 9/5 + 32)

temperature_in_celsius = 22 
f = temperature_in_celsius * 9/5 + 32
print("Temperature in celsius to fahrenheit:",f)

#What is a compiled language? What is an interpreted language? Explain pros and cons of each. How hybrid languages bring in advantages of both.*/

