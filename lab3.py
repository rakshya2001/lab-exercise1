# Give the integer N- the number of minutes that is passed since midnight.
# How many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours( between 0 and 23)
# and the number of minutes(between 0 and 59)
N = int(input("Enter the number of minutes"))
hours= N//60
minutes= N%60
print(f"hours is{hours}")
print(f"minutes is {minutes}")