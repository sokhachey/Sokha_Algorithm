# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
text = "454639"
countEven=0
countOdd=0
for i in range(len(text)):
    if int(text[i])%2==0:
        countEven+=1
    elif int(text[i])%2==1:
        countOdd+=1
print(countEven)
print(countOdd)

# Q2 - Sum all number 
text = "454639"
sum=0
for i in range(len(text)):
    sum+=int(text[i])
print(sum)

# Q3 - Sum only even number 
text = "454639"
sum=0
for i in range(len(text)):
    if int(text[i])%2==0:
        sum+=int(text[i])
print(sum)

# Q4 - Reverse 
text = "454639"
lastIndex=len(text)-1
result=" "
for i in range(len(text)):
    result+=text[lastIndex-i]
print(result)