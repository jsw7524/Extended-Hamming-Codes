import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

bits = input()
numberOf1=bits.count('1')
dataXor=0
for i,b in enumerate(bits):
    if b=='1':
        dataXor^=i
        
if 0==numberOf1%2:
    if 0==dataXor:
        print(bits) # no error
    else:
        print("TWO ERRORS")    
else:
    # one error occured in bits[dataXor]
    print(bits[:dataXor]+('0' if '1'==bits[dataXor] else '1') + bits[dataXor+1:]) 