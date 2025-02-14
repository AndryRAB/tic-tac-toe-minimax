class Noeud:
    
    def __init__(self, board=None, player_to_move='X'):
        self.board = board or [[' ', ' ', ' '] for _ in range(3)]
        self.player_to_move = player_to_move
        
    def is_full(self):
        # Vérifie que toutes les cases ne sont pas vides
        return all(cell != ' ' for row in self.board for cell in row)

    def check_winner(self):
        # Vérification des lignes
        for row in self.board:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return row[0]
        # Vérification des colonnes
        for col in range(3):
            if self.board[0][col] != ' ' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

        # Vérification des diagonales
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def is_terminal(self):
        # Le jeu est terminé s'il y a un gagnant ou si le plateau est plein
        return self.check_winner() is not None or self.is_full()

    def get_successor(self):
        if self.is_terminal():
            return []  # Aucun mouvement possible si le jeu est terminé
        
        # Détermination du prochain joueur
        next_player = 'O' if self.player_to_move == 'X' else 'X'
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    # Copie profonde du plateau pour éviter les modifications
                    new_board = [row[:] for row in self.board]
                    new_board[i][j] = self.player_to_move
                    yield Noeud(new_board, next_player)
    
    def eval(self,us):
        if self.check_winner() == us:
            return 1
        elif self.check_winner() == None:
            return 0
        else:
            return -1
            
    def __str__(self):
        return '\n'.join('|'.join(row) for row in self.board)
    
    def str_with_indent(self, indent):
        return '\n'.join(' ' * indent + '|'.join(row) for row in self.board)
    
    def __repr__(self):
        return f"Noeud({self.board}, {self.player_to_move})"
    
    