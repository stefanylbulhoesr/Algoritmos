def comprimentoMaior(str1,str2):
    if len(str1) > len(str2):
        return True
    else:
        return False
    
str1 = str(input("Digite a primeira string: "))
str2 = str(input("Digite a segunda string: "))
print(comprimentoMaior(str1,str2))