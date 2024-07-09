#get the input n from user and compute and print the folling value(log**2,cos,e**n)
import math

# Get input from the user
n=float(input("\nenter the number  : \n" ))
#compute log^2(n)
log_squared = math.log(n)**2
#compute cos(n)
cosine=math.cos(n)
#compute e^n (b=math.e**n)
exponential = math.exp(n)
print("\nlog**2 = ", log_squared ,"\ncos = ",cosine,"\ne = ",exponential )
print("\nlog^2 = {kogul:.2f}".format(kogul=log_squared),"\ncos ={b:.2f}".format(b=cosine),"\ne^n ={c:.2f}".format(c=exponential))
#print(txt)


  ### REFERNCES IN LINKS : https://www.w3schools.com/python/ref_string_format.asp 
