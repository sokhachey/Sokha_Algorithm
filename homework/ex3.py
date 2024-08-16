# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
text = input("Enter text: ")
isCotains = False
for i in range(len(text)):
    if text[i]==text[i].upper():
        isCotains = True
if isCotains:
    print("Yes")
else:
    print("No")