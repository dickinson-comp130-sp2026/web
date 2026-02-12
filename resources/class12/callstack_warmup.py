# Example of computing cups of flour in various situations, 
# designed for practising stack diagrams.

def add_extra(amount):
    extra = amount + 3
    print('Adding 3 extra cups to', amount, 'gives', extra, 'cups')
    divide_portions(extra)
    print('end of add_extra function')

def double_recipe(cups):
    doubled = cups * 2
    print(cups, 'cups doubled is', doubled, 'cups')
    add_extra(doubled)
    print('end of double_recipe function')


def divide_portions(total):
    servings = total / 4
    print('Dividing', total, 'cups into 4 portions gives', servings, 'cups each')
    print('end of divide_portions function')


flour = 6 # cups
double_recipe(flour)
print('end of main program')


# Acknowledgement: File created by Github Copilot, edited by John MacCormick. 
# Prompt was:
# Create a new Python file containing a fresh example that can be used to teach the idea of parameters and function calls that should be similar to the call_stack_demo.py file that is already open.