# Ex2 - String
# Enter text and display number of letter
text=str(input("Enter text:"))
count=0
for i in range(len(text)):
    count+=1
print(count)