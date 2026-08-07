#ask two numbers && operators and use if elif else to perform calculations 
#print the results 

x=int(input("1st number"))
y=int(input("2nd number"))
operators=(input("What operation (sum/div/sub/mult) do you want to perform on your two numbers??")).lower()
#.lower()  we use this so that a users input of either Sub or suB will be taken as sub

if operators == "sum":
  result = x+y
  print(f"Sum of the two numbers is {result}")
elif operators == "sub":
  result = x-y
  print(f"Subtraction of the two numbers is {result}")
elif operators == "div":
  result = x/y
  print(f"Division of the two numbers is {result}")
elif operators == "mult":
  result = x*y
  print(f"Multiplication of the two numbers is {result}")
else:
  print(f"Invalid Operator")
  

