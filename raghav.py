age= int(input("enter your age: "))
if(age>=18):
    print("Eligible to vote")
    if(age>=22):
        print("Eligible to marry")
    else:
        print("not eligible to Marry")
else:
    print("not eligible to vote")