# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# text="3 4 5 6"
# sum=" "
# for i in range(len(text)):
#     if text[i]!=" ":
#         sum+=text[i]
# print(sum)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"
text="3 4 5 6"
sum=0
result=" "
for i in range(len(text)):
    if text[i]!=" ":
        sum=int(text[i])*2
        result+=str(sum)+str(" ")
print(result)
