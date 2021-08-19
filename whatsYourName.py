
# sep='' removes all spaces in print function except spaces inside of " "

def printFullName (f, l):
    print("Hello", f, "", end='')
    print (l, "!", sep='', end='')
    print(" You just delved into python")

f_name = input ()
l_name = input ()

printFullName (f_name, l_name)
