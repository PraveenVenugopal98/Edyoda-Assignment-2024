a=int(input("Enter Start of number series : "))
b=int(input("Enter End of number series : "))
lst=range(a,b+1)
odd=[]
even=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
print("Even numbers are : ", even)
print("Odd numbers are : ", odd)
print("Total count of Even numbers : ", len(even))
print("Total count of odd numbers : ", len(odd))
    