#def inputs 
name=input("enter the patient's name :")
print("name")
cleaning= input("was cleaning performed?(y/n)")
print("cleaning done")
cavity=input("was cavity filling performed?(y/n)")
print("cavity done")
xray=input("was X ray  performed?(y/n)")
print("xray done")
#def different values
cleaning_rate=60
cavity_filling=200
x_ray=100
tax_rate=0.15
discount1=0.05
discount2=0.1



if(cleaning=="y"):
        print("cleaning_rate=60")
else:
        print("no")
    
if(cavity=="y"):
        print("cavity_filling=200")
else:
        print("no")
        
if(xray=="y"):
      
        print("x_ray=100")
else:
        print("no")
  
total=float(input("enter any value:"))
tax=total*tax_rate
total=total+tax
print("tax total:",tax)
 #for discount 
if(total>200):
        total=total-discount1
        print("5 per discount was applied")
elif(total>300):
        total=total-discount2
        print("10 per discount was applied")
        
print(" your total bill is :",total)
  
  
