```python
# Cria uma lista com as opções de sistemas operacionais da enquete.
# Cada elemento representa uma alternativa que o participante pode votar.
opcoes = ["windows", "unix", "linux", "netware", "mac os", "outros votos"]

# Cria uma lista com seis posições, uma para cada opção da enquete.
# Todas as posições começam com zero, pois nenhum voto foi registrado.
# A posição de cada contador corresponde à posição da opção em "opcoes".
votos = [0] * 6

# Apresenta o título da enquete ao participante.
print("Enquete: qual o melhor sistema operacional para uso em servidores?")

# Orienta o participante a digitar o número correspondente à sua escolha.
print("Digite um número correspondente à sua escolha:")

# Inicia um laço de repetição que mantém a votação ativa.
# O laço só termina quando o participante digita zero.
while True:

    # Percorre a lista de opções e apresenta cada uma com um número.
    # enumerate() fornece o índice de cada elemento.
    # start=1 faz a numeração começar em 1, em vez de 0.
    for i, opcao in enumerate(opcoes, start=1):

        # Exibe o número da alternativa seguido do nome do sistema.
        # Exemplo: "1 - windows".
        print(f"{i} - {opcao}")

    # Apresenta a opção zero, utilizada para encerrar a votação.
    print("0 - Encerrar a votação")

    # Inicia um bloco de tratamento de erros para validar a entrada.
    try:

        # Solicita o voto e converte a entrada digitada para um número inteiro.
        # int() converte textos numéricos, como "2", para o inteiro 2.
        voto = int(input("Seu voto: "))

        # Verifica se o participante digitou zero.
        # Se isso acontecer, o comando break encerra o laço de votação.
        if voto == 0:
            break

        # Verifica se o voto está entre 1 e 6, inclusive.
        # Esses números correspondem às seis opções disponíveis.
        elif 1 <= voto <= 6:

            # Subtrai 1 do voto para encontrar a posição correta na lista.
            # Por exemplo, o voto 1 corresponde ao índice 0.
            # O operador += incrementa o contador selecionado em uma unidade.
            votos[voto - 1] += 1

        # Executa este bloco se o número digitado não for válido.
        # Valores negativos ou maiores que 6 não são contabilizados.
        else:

            # Informa ao participante quais números são aceitos.
            print("Valor inválido, digite um número de 0 a 6.")

    # Captura o erro que ocorre quando a entrada não pode ser convertida
    # para um número inteiro, como quando o participante digita "abc".
    except ValueError:

        # Informa que a entrada precisa ser um número inteiro.
        # A votação continua porque o erro foi tratado.
        print("Entrada inválida, digite um número inteiro.")

# Calcula a quantidade total de votos registrados.
# sum() soma todos os valores armazenados na lista "votos".
total_votos = sum(votos)

# Verifica se a soma dos votos é igual a zero.
# Isso acontece quando a votação é encerrada sem nenhum voto válido.
if total_votos == 0:

    # Informa que nenhum voto foi contabilizado.
    print("Nenhum voto foi computado.")

# Executa este bloco quando existe pelo menos um voto registrado.
else:

    # Exibe o título da seção de resultados.
    # \n insere uma quebra de linha antes do texto.
    print("\nResultado da votação:")

    # Percorre todas as opções, utilizando seus índices originais.
    # enumerate() começa em zero por padrão.
    for i, opcao in enumerate(opcoes):

        # Calcula a porcentagem de votos recebidos pela opção atual.
        # Divide os votos da opção pelo total de votos e multiplica por 100.
        percentual = (votos[i] / total_votos) * 100

        # Apresenta o nome da opção, sua quantidade de votos
        # e a porcentagem correspondente.
        # {votos[i]} mostra o total de votos da opção.
        # :.2f formata a porcentagem com duas casas decimais.
        # O texto "voto(s)" é utilizado independentemente da quantidade.
        print(f"{opcao}: {votos[i]} voto(s) - {percentual:.2f}%")
```
