def ctof(c):
        return(round(((9/5)*c)+32,3))
def ftoc(f):
        return(round((5/9)*(f-32),3))
def ktof(k):
        return(round(((9/5)*(k-273))+32,3))
def ftok(f):
        return(round(((5/9)*(f-32))+273,3))
def ctok(c):
        return(round(c+273,3))
def ktoc(k):
        return(round(k-273,3))

def fun():
        print("temperature conversion")
        print("1 ctof")
        print("2 ftoc")
        print("3 ktof")
        print("4 ftok")
        print("5 ktoc")
        print("6 ctok")
        values=list()
        while(True):     
                ch=input("enter your option:")
                if (ch =='1'):
                        c=input("enter temperature in celcius:")
                        f=str(ctof(float(c)))
                        print("temperature in fahrenheit is:"+f)
                        values.append((str(c+'c'),str(f+'f')))
                elif(ch =='2'):
                        f=input("enter temperature in fahreheit:")
                        c=str(ftoc(float(f)))
                        print("temperature in celcius is:"+c)
                        values.append((str(f+'f'),str(c+'c')))  
                elif(ch=='3'):
                        k=input("enter temperature in kelvin:")
                        f=str(ktof(float(k)))                           
                        print("temperature in fahrenheit is:"+f)
                        values.append((str(k+'k'),str(f+'f')))
                elif(ch=='4'):
                        f=input("enter temperature in fahrenheit:")
                        k=str(ftok(float(f)))
                        print("temperature in kelvin is:"+k)
                        values.append((str(f+'f'),str(k+'k')))
                elif(ch=='5'):
                        k=input("enter temperature in kelvin:")
                        c=str(ktoc(float(k)))
                        print("temperature in celcius is:"+c)
                        values.append((str(k+'k'),str(c+'c')))
                elif(ch=='6'):
                        c=input("enter temperature in celcius:")
                        k=str(ctok(float(c)))
                        print("temperature in kelvin is:"+k)
                        values.append((str(c+'c'),str(k+'k')))
                else :
                        print("worng option")

                choice=input("once again [y/n]:")
                while(True):             
                        if(choice=='n' or choice=='N' or choice=='Y' or choice=='y'):
                                break
                        else:
                                print("wrong choice.")
                                choice=input("once again [y/n]:")
                if(choice=='n' or choice=='N'):
                        print(values)                   
                        break

fun()
