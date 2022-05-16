introString=input("enter string:")
charecterCount=0
wordCount=1
for i in introString:
    charecterCount=charecterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("number of words ")
print(wordCount)
print("number of charecters")
print(charecterCount)
