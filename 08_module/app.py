from marketing.resale import resale
from marketing.predection import future_sales
from marketing.resale.resale import calc_resales_value
from marketing.predection import calc_marketing_expense
from pprint import pprint
import sys
from sales import calc_shipping
# to see all them to see objects defined in any module press CTRL+Space after import
# using comma and module name to import multiple module
# use * to import everything
# import moduleName will import everything but to access object we eill have to use moduleName.Object we want to use
calc_shipping()

# after running python app.py an new folder inside current directory will be created
# that folder will contain compiled version of modules that we have imported in our program
# it will not compile everytime we run app.py
# it will first check for module date and if it is later than compiled one then only it will compile again


# if we import something and it can't find in current directory then it will try to look for relevent file in predefined directory
# which is listed in sys.path
# import sys
# from pprint import pprint
# return a list of predefined path where python will look for files being imported
data = sys.path
pprint(data, width=1)  # to see predefined directory

# use of subdirectory to store packages in arranged manner
# but then we must have to add a file named __init__.py to indicate python to treat that folder as package
# from marketing.predection import calc_marketing_expense
future_sales()


# we can even make folders inside folder in the same process
# from marketing.resale.resale import calc_resales_value
calc_resales_value()


# Intra-package refrences
# ABSOLUTE PATH
# marketing->predection.py is using function form current directory/hr/people.py function
"""
.. for one level up
. for current directory
"""
# from marketing.predection import calc_marketing_expense
calc_marketing_expense()

# sometimes we dont know all the methods and functions defined in any package
# so we can use dir(packageName) to find out what are there
# example:
# from marketing.resale import resale
pprint(dir(resale), width=1)
""" OUTPUT:
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'calc_resales_tax',
 'calc_resales_value']
"""

print(resale.__name__)  # to get name of the file
print(resale.__package__)  # to get name of the package
print(resale.__file__)  # to get path of the file

# now we know that name of the module is in __name__ and we can always get it
# in any file if we call any function or execute any statement then it will be printed only once during compilation
# and later on it will not be executed untill next compilation on changes made in file
# we can utilize __name__ to execute some function for testing in that file only
