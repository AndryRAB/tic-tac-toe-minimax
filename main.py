from noeud import Noeud  

def print_tree(root, indent= 0, depth=1):
    print(root.str_with_indent(indent))
    print()
    if depth > 1:
        for succ in root.get_successor():
            print_tree(succ, indent + 4, depth - 1)
    

def minimax(node, depth, us='X'):
    if depth == 0 or node.is_terminal():
        return (node.eval(us), None)
    if node.player_to_move == us:
        maxEval = -1000
        best_move = None
        for child in node.get_successor():
            eval, _ = minimax(child, depth - 1, us)
            if eval > maxEval:
                maxEval = eval
                best_move = child            
        return (maxEval, best_move)                
    else:
        minEval = 1000
        best_move = None
        for child in node.get_successor():
            eval, _ = minimax(child, depth - 1, us)
            if eval < minEval:
                minEval = eval
                best_move = child
        return (minEval, best_move)
   

def alphabeta(node, depth, alpha, beta, us='X'):
    if depth == 0 or node.is_terminal():
        return (node.eval(us), None)
    if node.player_to_move == us:
        maxEval = -1000
        best_move = None
        for child in node.get_successor():
            eval, _ = alphabeta(child, depth - 1, alpha, beta, us)
            if eval > maxEval:
                maxEval = eval
                best_move = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return (maxEval, best_move)
    else:
        minEval = 1000
        best_move = None
        for child in node.get_successor():
            eval, _ = alphabeta(child, depth - 1, alpha, beta, us)
            if eval < minEval:
                minEval = eval
                best_move = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return (minEval, best_move)
    

def main():
    nd = Noeud()
    print_tree(nd, depth=3)
    print(minimax(nd, 1000))
    print(alphabeta(nd, 1000, -1000, 1000))
    
    
if __name__ == "__main__":
    main()
