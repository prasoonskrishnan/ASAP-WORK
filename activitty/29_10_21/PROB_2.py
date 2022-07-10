word = input('Enter a word: ')
if len(word)<3:
    print(word,'has less than 3 letters')
elif len(word)>=3 and len(word)<=5:
    print(word,'has letters b/w 3 & 5')
else:
    print(word,'has more than 5 letters')
