sum=0
n=1 
while n<100:
    if n>10:
        print('END')
        break
    else:
        print('n=',n)
        sum=sum+n
        n=n+1
print('总计:',sum)

n=0
while n<10:
	n=n+1
	if n%2==0:
		continue
	else:
		print(n)

