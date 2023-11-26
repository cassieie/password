password = input('請輸入密碼:')
x = 1
if password == 'a123456':
	print('成功')
else:
	while password != 'a123456' and x < 3:
		print('密碼錯誤')
		input('請重新輸入:')
		x = x+1