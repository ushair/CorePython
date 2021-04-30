import re,math
import numpy as np


exp= input("enter expression:")
print("before Operation : {}".format(exp))

while True:
    sq_regex= "sq\(\d*\.?\d*\)"

    sq_found = re.search(sq_regex,exp)
    
    if not sq_found:
        break
    
    sq_string = exp[sq_found.start():sq_found.end()]
    
    digit_found = re.search("\d+",sq_string)
    
    if digit_found:
        digit = sq_string[digit_found.start() : digit_found.end()]
        
        try:
            digit = float(digit)
        except:
            print("Enter Float value in square function")
            break
        
        val= digit * digit
        exp = exp[:sq_found.start()] + str(val) + exp[sq_found.end():]
    else:
        print("No Digit Inside Square Function")
        break
    
    print("After Operation : {}".format(exp))

while True:
    sqrt_regex="sqrt\(\d*\.?\d*\)"

    sqrt_found = re.search(sqrt_regex,exp)
    
    if not sqrt_found:
        break
    
    sqrt_string = exp[sqrt_found.start():sqrt_found.end()]
    
    digit_found = re.search("\d+",sqrt_string)
    
    if digit_found:
        digit = sqrt_string[digit_found.start() : digit_found.end()]
        
        try:
            digit = float(digit)
        except:
            print("Enter  value in add function")
            break
        
        val= math.sqrt(digit)
        exp = exp[:sqrt_found.start()] + str(val) + exp[sqrt_found.end():]
    else:
        print("No Digit Inside add Function")
        break
    
    print("After Operation : {}".format(exp))

#reciprocal

while True:
    repl_regex="recp\(\d*\.?\d*\)"

    repl_found = re.search(repl_regex,exp)
    
    if not repl_found:
        break
    
    repl_string = exp[repl_found.start():repl_found.end()]
    
    digit_found = re.search("\d+",repl_string)
    
    if digit_found:
        digit = repl_string[digit_found.start() : digit_found.end()]
        
        try:
            digit = float(digit)
        except:
            print("Enter  value in add function")
            break
        
        val= np.reciprocal(digit)
        exp = exp[:repl_found.start()] + str(val) + exp[repl_found.end():]
    else:
        print("No Digit Inside add Function")
        break
    
    print("After Operation : {}".format(exp))

print("\n Result of expression : {}".format(eval(exp)))