import random
import os

class ticTacToe:
    def __init__(self):
        self.reset()
        self.done = ""
    
    def print_board(self):
        print("======= JOGO DA VELHA =======")
        print("               COLUNA")
        print("            0     1     2")

        print("        0", " ", self.board[0][0]," | ", self.board[0][1]," | ", self.board[0][2])
        print("           ---------------")
        print("LINHA   1", " ", self.board[1][0]," | ", self.board[1][1]," | ", self.board[1][2])
        print("           ---------------")
        print("        2", " ", self.board[2][0]," | ", self.board[2][1]," | ", self.board[2][2])
        print("==============================")
        
    
    def reset(self):
        self.board = [[" ", " "," "],[" "," ", " "],[" "," ", " "]]
        self.done = ""
    
    def check_win_or_draw(self):
        dict_win = {}
        
        for i in ["X", "O"]:
            # linha horinzontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] ==  self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] ==  self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] ==  self.board[2][2] == i) or dict_win[i]
            
            # linha vertical
            dict_win[i] = (self.board[0][0] ==  self.board[1][0] ==  self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] ==  self.board[1][1] ==  self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] ==  self.board[1][2] ==  self.board[2][2] == i) or dict_win[i]
            
            # linha diagonal
            dict_win[i] = (self.board[0][0] ==  self.board[1][1] ==  self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] ==  self.board[1][1] ==  self.board[2][0] == i) or dict_win[i]
            
        if dict_win["X"]:
            self.done = "X"
            print("Jogador X venceu!")
            return
        elif dict_win["O"]:
            self.done = "O"
            print("Jogador O venceu!")
            return
        
        
        c = 0
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break

        if c == 0:
            self.done = "Empate"
            print("Empate!")
            return
        
        
    def get_player_move(self):
        invalid_mode = True
        while invalid_mode:
            try:
                row = int(input("Digite a linha (0, 1 ou 2): "))
                col = int(input("Digite a coluna (0, 1 ou 2): "))

                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Entrada inválida! Tente novamente.")
                    
                if self.board[row][col] != " ":
                    print("Posição já ocupada! Tente novamente.")
                    continue
            except (ValueError, IndexError):
                print("Entrada inválida! Tente novamente.")
                continue
    
            invalid_mode = False
        self.board[row][col] = "X"
        
        
    def make_move(self):
        list_moves = []
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))
                
                
        if len(list_moves) > 0:
            x,y = random.choice(list_moves)
            self.board[x][y] = "O"
    
    
    
tic_tae_toe = ticTacToe()
tic_tae_toe.print_board()


next = 0

while next == 0:
    os.system("cls" if os.name == "nt" else "clear")
    tic_tae_toe.print_board()
    
    while tic_tae_toe.done == "":
        tic_tae_toe.get_player_move()
        tic_tae_toe.make_move()
        tic_tae_toe.check_win_or_draw()
        os.system("cls" if os.name == "nt" else "clear")
        tic_tae_toe.print_board()
        tic_tae_toe.check_win_or_draw()
        
    print("Digite 1 para encerrar o jogo ou 0 para reiniciar")
    next = int(input()) 
    
    if next == 1:
        print("Obrigado por jogar!")
        break
    else :
        tic_tae_toe.reset()
        next = 0
    
    
    