# In this file, identify all instances of
# 1. function calls
# 2. constructor calls
# 3. method calls
# Note: You are not expected to have any familiarity with the fractions and time modules. 
import fractions
import time

start = time.localtime()
one_half = fractions.Fraction(1,2)
two_thirds = fractions.Fraction(2,3)
result = 9 * two_thirds
if result.is_integer():
    result = int(result)
end = time.localtime()


