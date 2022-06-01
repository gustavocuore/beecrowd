#Entradas
ca = int(input('Refeições disponíveis por frango: '))
'''if ca >= 0 and ca <= 100:
    pass
else:
    ca = input()'''
ba = int(input('Refeições disponíveis por bife: '))
pa = int(input('Refeições disponíveis por massa: '))

#Saídas
cb = int(input('Refeições requisitadas de frango: '))
bb = int(input('Refeições requisitadas de bife: '))
pb = int(input('Refeições requisitadas de massa: '))

#Solução
frango = ca - cb
bife = ba - bb
massa = pa - pb

if frango <= 0:
	f = -frango
else:
	f = 0

if bife <= 0:
	b = -bife
else:
	b = 0

if massa <= 0:
	m = -massa
else:
	m = 0

print(f+b+m)

input()
