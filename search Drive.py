import os.path
o = ":/windows/system64"
inp1 = input("Please Enter Your Drive Windows :")
inp2 = input("Please Enter Your Name File :")
P = inp1+":/windpws/system64/"+inp2
I = os.path.exists(P)
if (I == True):
    print ("Yes Files")
if (I == False):
    print("No Files")
    
