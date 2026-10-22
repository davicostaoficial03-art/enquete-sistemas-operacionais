opcoes = ["windows", "unix", "linux", "netware", "mac os", "outros votos"]
votos = [0] * 6

print("Enquete: qual o melhor sistema operacional para uso em servidores?")
print("Digite um número correspondente à sua escolha:")

while True:
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")
    print("0 - Encerrar a votação")

    try:
        voto = int(input("Seu voto: "))
        if voto == 0:
            break
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1
        else:
            print("Valor inválido, digite um número de 0 a 6.")
    except ValueError:
        print("Entrada inválida, digite um número inteiro.")

total_votos = sum(votos)
if total_votos == 0:
    print("Nenhum voto foi computado.")
else:
    print("\nResultado da votação:")
    for i, opcao in enumerate(opcoes):
        percentual = (votos[i] / total_votos) * 100
        print(f"{opcao}: {votos[i]} voto(s) - {percentual:.2f}%")
