print("-------hello user welcome to temperature converter-------")
n=int(input("enter number which you want to convert"))
print("\n","select no in which scale you want to convert temperature ")
print("\n","1. celsisus to fahrenheit","\n","2.Fahrenheit to celsisus","\n","3.celsisus to kelvin","\n","4.kalvin to celsisus")
ask=int(input("enter temperature conversion no"))

def CF():
    f=(1.8*n)+32
    print("temperature in fahrenheit is ", f,"F")

def FC():
    c=(n-32)*0.555
    print("temperature in celsisus is ", c,"C")

def CK ():
    k=(n+273)
    print("temperature in Kelvin is",k,"K")

def KC():
    x=(n-273)
    print("temperature in celsisus is ", x,"C")

if ask==1:
    CF()
if ask==2:
    FC()
if ask==3:
    CK()
if ask==4:
    KC()
input()


