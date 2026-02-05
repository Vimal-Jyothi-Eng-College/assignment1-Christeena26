list=[10,20,30,40,50]
key=int(input("Enter the element to search:"))
found=False
for i in range(len(list)):
    if list[i]==key:
       print("Element found at position:",i)
       found=True
       break
if not found:
    print("Element not found")