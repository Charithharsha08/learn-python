# import my_calculator type 1
#import my_calculator.addition, my_calculator.substraction
#add_result = my_calculator.addition.add(10, 20)
#substract_result = my_calculator.substraction.substract(20, 30)


# import my_calculator type 2
# from my_calculator import addition, substraction
# add_result = addition.add(10, 20)
# substract_result = substraction.substract(20, 30)


# import my_calculator type 3
# from my_calculator.addition  import add
# from my_calculator.substraction import substract

# after intializing __init__.py file in my_calculator package 
# We can import addition and substraction modules directly from my_calculator
#from my_calculator import add, substract

#from my_calculator import *
import my_calculator

add_result = my_calculator.add(10, 20)
substract_result = my_calculator.substract(20, 30)

print(add_result)
print(substract_result)