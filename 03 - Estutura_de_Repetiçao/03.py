"""
03 - Faça um programa que leia e valide as seguintes informações:
a - Nome: maior que 3 caracteres;
b - Idade: entre 0 e 150;
c - Salário: maior que zero;
d - Sexo: 'f' ou 'm';
e - Estado Civil: 's', 'c', 'v', 'd'; """

nome = str(input("Digite o seu nome: ")).upper()
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu sálario: "))
sexo = str(input("Digite F para feminino ou M para masculino: ")).upper()
estado_civil = str(
    input(
        """Digite o Estado civil:
S para solteiro(a)
C para casado(a)
V para viuvo(a)
D para divorciado(a)
Digite aqui: """
    )
).upper()

contador = len(nome)
print("\n")

while (contador < 3 and idade < 0 or idade > 150 and salario < 0 and sexo != "F" and sexo != "M" and estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D"):
    print("dados invalido! digite novamente!!!!")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite a sua idade: "))
    salario = float(input("Digite o seu sálario: "))
    sexo = str(input("Digite F para feminino ou M para masculino: ")).upper()
    estado_civil = str(
        input(
            """Digite o Estado civil:
    S para solteiro(a)
    C para casado(a)
    V para viuvo(a)
    D para divorciado(a)
    Digite aqui: """
        )
    ).upper()
    print("\n")
    
else:
    print("Dados validados com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salario: R${salario:.2f}")
    if(sexo == "F"):
        print("Sexo: Feminino")
    else:
        print("Sexo: Masculino")
    if(estado_civil == "S"):
        print("Estado civil: Solteiro")
    elif(estado_civil == "C"):
        print("Estado civil: Casado")
    elif(estado_civil == "V"):
        print("Estado civil: Viuvo")
    else:
        print("Estado civil: Divorciado")
