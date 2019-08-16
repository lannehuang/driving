contury = input('你來自哪個國家： ')
age = input('你的年齡是： ')
age = int(age)
if contury == 'taiwan' :
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif contury == 'usa' :
	if age >= 16 :
		print('你可以考駕照')
	else :
		print('你還不能考駕照')
