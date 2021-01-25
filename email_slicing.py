user_input=str(input('Enter your user name : '))
username=user_input[:user_input.index('@')]
domain=user_input[user_input.index('@')+1:]
print('Your name is '+username)
print('Your domain is '+domain)
