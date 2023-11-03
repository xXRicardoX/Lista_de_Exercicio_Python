'''4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante'''

letra = str(input("Digite uma letra para saber se e consoante ou vogal: "))

vogal = ["a","e","i","o","u","A","E","I","O","U"]
consoante = ["b","c","d","f","g","h","j","l","m","n","p","q","r","s","t","v","x","y","z","B","C","D","F","G","H","J","L","M","N","P","Q","R","S","T","V","X","Y","Z"]


if (letra in vogal):
    print(f"A Letra digitada {letra} é uma vogal é uma vogal")
elif(letra in consoante):
    print(f"A Letra digitada {letra} é uma consoante")
else:
    print("Digite uma letra apenas!!!")