'Faça um program que mostre os n termos da série a seguir'
's = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 ... + n/n'
n = int(input("Deseja ir até qual numerador? "))
den = 0
soma = 0
for num in range (1,n+1):
    den = (num * 2) - 1
    frac = num / den
    print(num, "/", den, "=", frac, "=" )
    soma = frac + soma
    print(soma, "+")

