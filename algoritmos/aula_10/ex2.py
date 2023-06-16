def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

#interatividade:
num = int(input('Digite o valor de n para obter o n-ésimo termo da sequência de Fibonacci: '))
resultado = fibonacci(num)
print('O', num, 'termo da sequência de Fibonacci é', resultado)
