import os

# Função para imprimir a grade na tela
def printGrid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

# Função para verificar se a grade está completamente preenchida
def isFull(grid):
    return all(cell != ' ' for row in grid for cell in row)

# Função para verificar se o jogador 'g' ganhou
def checkWinner(grid, g):
    # Verificar linhas
    for row in grid:
        if all(cell == g for cell in row):
            return True
    # Verificar colunas
    for col in range(3):
        if all(grid[row][col] == g for row in range(3)):
            return True
    # Verificar diagonal principal
    if all(grid[i][i] == g for i in range(3)):
        return True
    # Verificar diagonal secundária
    if all(grid[i][2-i] == g for i in range(3)):
        return True
    return False

# Função para criar o arquivo de pontuações se não existir
def createScoresFile(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

# Função para salvar as pontuações dos jogadores em um arquivo
def saveScores(players_scores, filename):
    with open(filename, 'w') as file:
        for player, score in players_scores.items():
            file.write(f"{player}:{score}\n")

# Função para carregar as pontuações dos jogadores de um arquivo
def loadScores(filename):
    if not os.path.exists(filename):
        return {}
    players_scores = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                player, score = line.split(':')
                players_scores[player] = int(score)
    return players_scores

# Função para exibir as pontuações do arquivo
def displaySavedScores(filename):
    players_scores = loadScores(filename)
    print("Pontuações armazenadas:")
    for player, score in players_scores.items():
        print(f"{player}: {score}")

# Função para jogar o jogo da velha
def playTicTacToe():
    # Obter os nomes dos jogadores
    player1 = input("Nome do jogador 1: ").replace(':', '').replace('\n', '')
    player2 = input("Nome do jogador 2: ").replace(':', '').replace('\n', '')

    # Definir o nome do arquivo para salvar as pontuações
    filename = "pontuacoes.txt"
    # Criar o arquivo de pontuações se não existir
    createScoresFile(filename)
    # Carregar as pontuações dos jogadores do arquivo
    players_scores = loadScores(filename)

    # Definir as pontuações iniciais como 0, se os nomes não estiverem no arquivo
    if player1 not in players_scores:
        players_scores[player1] = 0
    if player2 not in players_scores:
        players_scores[player2] = 0


    # Loop principal do jogo
    while True:
        # Criar a grade vazia
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        printGrid(grid)
        # Variável para controlar o turno do jogador
        player_turn = 1

        # Loop para cada jogada
        while True:
            # Determinar o símbolo do jogador atual (X ou O)
            current_player = 'X' if player_turn == 1 else 'O'
            player_name = player1 if player_turn == 1 else player2

            # Perguntar a posição onde o jogador deseja colocar seu símbolo
            while True:
                try:
                    x, y = map(int, input(f"{player_name}, linha e coluna (1-3 separados por espaço): ").split())

                    if 1 <= x <= 3 and 1 <= y <= 3 and grid[x-1][y-1] == ' ':
                        break
                    else:
                        print("Posição inválida. Escolha uma posição vazia dentro da grade.")
                except ValueError:
                    print("Entrada inválida. Digite dois números de 1 a 3 separados por espaço.")

            # Colocar o símbolo do jogador na grade
            grid[x-1][y-1] = current_player
            # Mostrar a grade atualizada
            printGrid(grid)

            # Verificar se o jogador atual ganhou
            if checkWinner(grid, current_player):
                print(f"Parabéns, {player_name}! Você ganhou!")
                # Atualizar a pontuação do jogador vencedor
                players_scores[player_name] = players_scores.get(player_name, 0) + 1
                break

            # Verificar empate
            if isFull(grid):
                print("Empate!")
                # Atualizar a pontuação dos dois jogadores em caso de empate
                players_scores[player1] = players_scores.get(player1, 0) + 1
                players_scores[player2] = players_scores.get(player2, 0) + 1
                break
            

            # Alternar o turno do jogador
            player_turn = 3 - player_turn

        # Salvar as pontuações
        saveScores(players_scores, filename)
        # Perguntar se os jogadores querem ver as pontuações armazenadas
        show_scores = input("Desejam ver as pontuações armazenadas? (s/n): ").lower()
        if show_scores == 's':
            displaySavedScores(filename)
        
        # Perguntar se os jogadores querem jogar novamente
        play_again = input("Desejam jogar novamente? (s/n): ").lower()
        if play_again != 's':
            break

# Iniciar o jogo se este script for executado diretamente
if __name__ == "__main__":
    playTicTacToe()


#Creditos:(todos canais do youtube que me ensinaram sobre o jogo e como cria-lo no python) 
#CFBCursos
#I DO CODE
#programando com roger 
# A maior dificuldade que eu tive foi em fazer salvar as pontuações dos jogadores.
#obrigado pela oportunidade s2.

