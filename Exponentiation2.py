
def exp(base,exponent):
	result=base**exponent
	return result
print("---------------------------------------")
exponent=4
base= 3 
for i in range (1,exponent+1):
	print( exp(base,i))


print("---------------------------------------") 
base=int(input("Enter a number that will be our base\n "))
exponent==int(input("Enter a number that will be our exponent\n "))
for i in range (1,exponent+1):
	r=( exp(base,i))

print("Our result is %d"%(r))
