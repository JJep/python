def triangles():
	count = 1
	if count == 1 :
		count += 1
		t = [1]
		yield t 
	if count == 2 :
		t = [1,1]
		yield t 
		count += 1
	if count > 2:	
		while True:
			# print('t = ', t)
			a = []
			# print('============' )
			for i in range(len(t)) :
				# print('i = ', i)
				# print('a[',i-1,'] = ',a[i-1])
				# print('a = ', a)
				if i > 0 :
					a.append(t[i-1] + t[i])
				else:
					a.append(1)
				# print('a = ', a)
			a.append(1)
				# print(t[i-1])
			t = a
			yield t
	return 'done'
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

