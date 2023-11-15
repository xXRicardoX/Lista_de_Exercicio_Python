"""02 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

nome = input("Digite o seu nome: ")
senha = input("Digite a sua senha: ")

while(nome == senha):
    print("A senha não pode ser o mesmo do nome!!\nDigite a senha novamente\n")
    senha = input("Digite a sua senha: ")
    
else:
    print("Senha valida")
    