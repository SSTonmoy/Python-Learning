# Write a program to read the text from a given file ‘poems.txtʼ
# And find out whether it contains the word ‘twinkleʼ.
f = open("Chapter09/poems.txt", 'r')
text = f.read()
print(text)
if "twinkle" in text:
    print("Word found")
else:
    print("Word not found")
f.close()
