#x14 -Faixa etaria

idade = int(imput("Digite a sua idade: "))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")

elif idade > 60:
    print("idoso")