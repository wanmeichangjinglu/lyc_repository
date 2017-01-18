high=float(input('输入你的身高（米）：'))
heavy=float(input('输入你的体重（kg）：'))
high_2=high*high
BMI=heavy/high_2
if BMI<18.5:
	print('过轻')
elif BMI>=18.5 and BMI<25:
	print('正常')
elif BMI>=25 and BMI<28:
	print('过重')
elif BMI>=28 and BMI<32:
	print('肥胖')
elif BMI>=32:
	print('严重肥胖')