user_inp=str(input('Input a phrase : ')).lower()
#user_inp=user_inp
parts=user_inp.split()

a=''
pass_words=['and','of','in','&']
for i in parts:
    if i not in pass_words:
        a=a+str(i[0]).upper()
    

print(a)
    

