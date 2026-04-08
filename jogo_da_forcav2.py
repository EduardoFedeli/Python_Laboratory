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

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca (7 estágios no total)
    stages = [
        # estágio 6 - final (perdeu)
        """
                ----------
                |        |
                |        |
                |       \O/
                |        |
                |       / \\
                |       
        ________|______
        """,
        # estágio 5
        """
                ----------
                |        |
                |        |
                |       \O/
                |        |
                |       / 
                |       
        ________|______
        """,
        # estágio 4
        """
                ----------
                |        |
                |        |
                |       \O/
                |        |
                |        
                |       
        ________|______
        """,
        # estágio 3
        """
                ----------
                |        |
                |        |
                |       \O
                |        |
                |        
                |       
        ________|______
        """,
        # estágio 2
        """
                ----------
                |        |
                |        |
                |        O
                |        |
                |        
                |       
        ________|______
        """,
        # estágio 1
        """
                ----------
                |        |
                |        |
                |        O
                |        
                |        
                |       
        ________|______
        """,
        # estágio 0 (início, sem erros)
        """
                ----------
                |        |
                |        |
                |        
                |        
                |        
                |       
        ________|______
        """
    ]
    
    return stages[chances]


def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    lista_palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Sorteia uma palavra da lista
    palavra_aleatoria = random.choice(lista_palavras)

    # Cria uma lista com "_" no lugar das letras da palavra
    letras_descobertas = ['_' for _ in palavra_aleatoria]

    # Número máximo de chances
    chances = 6

    # Lista para armazenar letras erradas
    letras_erradas = []

    # Loop do jogo
    while chances > 0:
        limpa_tela()
        
        # Mostra a forca de acordo com as chances
        print(display_hangman(chances))

        # Mostra as letras já descobertas
        print('Palavra:', ' '.join(letras_descobertas))

        # Mostra número de chances e letras já erradas
        print('\nChances restantes:', chances)
        print('Letras erradas:', ', '.join(letras_erradas))

        # Jogador digita uma letra
        tentativa = input('\nDigite uma letra: ').lower()

        # Se a letra já foi tentada
        if tentativa in letras_erradas or tentativa in letras_descobertas:
            print("\nVocê já tentou essa letra. Tente outra!")
            input("\nPressione ENTER para continuar...")
            continue

        # Se a letra estiver na palavra
        if tentativa in palavra_aleatoria:
            for index, letra in enumerate(palavra_aleatoria):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Vitória
        if '_' not in letras_descobertas:
            limpa_tela()
            print(display_hangman(chances))
            print('\nPalavra:', ' '.join(letras_descobertas))
            print('\n🎉 Parabéns! Você venceu! A palavra era:', palavra_aleatoria)
            break
    else:
        # Derrota
        limpa_tela()
        print(display_hangman(chances))
        print('\n💀 Você perdeu! A palavra era:', palavra_aleatoria)


# Bloco principal
if __name__ == "__main__":
    game()
    print('\nObrigado por jogar!')
