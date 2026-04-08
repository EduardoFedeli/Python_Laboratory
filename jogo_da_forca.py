import random
from os import system, name

# Função para limpar a tela a cada jogada
def limpa_tela():
    # Se o sistema for Windows
    if name == 'nt':
        _ = system('cls')
    # Se for Mac ou Linux
    else:
        _ = system('clear')

def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo (todas em minúsculo para evitar bug com .lower())
    lista_palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Sorteia uma palavra da lista
    palavra_aleatoria = random.choice(lista_palavras)

    # Cria uma lista com "_" no lugar das letras da palavra
    letras_descobertas = ['_' for _ in palavra_aleatoria]

    # Número máximo de chances
    chances = 6

    # Lista para armazenar letras erradas
    letras_erradas = []

    # Loop do jogo (continua enquanto o jogador ainda tiver chances)
    while chances > 0:
        # Mostra as letras já descobertas
        print(''.join(letras_descobertas))

        # Mostra número de chances e letras já erradas
        print('\nChances restantes:', chances)
        print('Letras erradas:', letras_erradas)

        # Jogador digita uma letra (convertida para minúscula)
        tentativa = input('\nDigite uma letra: ').lower()

        # Se a letra estiver na palavra
        if tentativa in palavra_aleatoria:
            # Substitui "_" pela letra correta em todas as posições
            for index, letra in enumerate(palavra_aleatoria):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else: 
            # Se errou, perde uma chance
            chances -= 1
            letras_erradas.append(tentativa)

        # Condição de vitória: se não existir mais "_" na lista
        if '_' not in letras_descobertas:
            print('\nVocê venceu, a palavra era', palavra_aleatoria)
            break
    else:
        # Esse bloco "else" roda quando o while termina sem break (ou seja, quando perdeu todas as chances)
        print('\nVocê perdeu, a palavra era:', palavra_aleatoria)

# Bloco principal (executa o jogo quando o arquivo for rodado diretamente)
if __name__ == "__main__":
    game()
    print('Obrigado por jogar!')
