O_ROCK, O_PAPER, O_SCISS = "A", "B", "C" 
P_ROCK, P_PAPER, P_SCISS = "X", "Y", "Z"

RULES_PLAYER = {O_ROCK:P_PAPER, O_PAPER:P_SCISS, O_SCISS:P_ROCK}
RULES_OPP = {P_PAPER:O_SCISS, P_SCISS:O_ROCK, P_ROCK:O_PAPER}

PLAYER_LOSS = {O_ROCK:P_SCISS,O_PAPER:P_ROCK,O_SCISS:P_PAPER} 

INDEX = {P_ROCK:1, P_PAPER:2, P_SCISS:3} 

STRINGS = {O_ROCK:"Rock",O_PAPER:"Paper",O_SCISS:"Scissor",P_ROCK:"Rock",P_PAPER:"Paper",P_SCISS:"Scissor"} 

TRANSLATE = {O_ROCK:P_ROCK, O_PAPER:P_PAPER, O_SCISS:P_SCISS} 

def ts(s):
    return STRINGS[s]

def print_bool(b):
    if (b):
        return "Yes!"
    return "No"

def print_log(opp, player, player_should, opp_should, player_won, opp_won,score):
    print("Player played: ", ts(player), "\tOpp played: ", ts(opp), "\tPlayer should: ", ts(player_should), "\tOpp should: ", ts(opp_should), "\tPlayer won?",print_bool(player_won), "\tOpp won? ",print_bool(opp_won), "\tScore: ", score) 

def evaluate_round(opp, player): 
    score = 0   
    did_win_player = RULES_PLAYER[opp] == player
    did_win_opp = RULES_OPP[player] == opp 
    if (did_win_player):
        score += 6 
    elif (did_win_opp):
        score += 0 
    else:
        score += 3 
    score += INDEX[player]
    
    print_log(opp, player, RULES_PLAYER[opp], RULES_OPP[player], did_win_player, did_win_opp, score); 

    return score 

LOSS = "X" 
DRAW = "Y" 
WIN = "Z" 

def evaluate_strag(opp, stat):
    player = "" 
    score = 0 
    if (stat == LOSS):
        player = PLAYER_LOSS[opp]
        score = 0 
    if (stat == DRAW):
        player = TRANSLATE[opp]
        score = 3 
    if (stat == WIN):
        player = RULES_PLAYER[opp] 
        score = 6 
    score += INDEX[player] 
    return score 

def read_and_eval(fname, eval_func):
    total_score = 0
    with open(fname, "r") as inputfile:
        for line in inputfile:
            opp, player = line.split(" ")
            player = player[0]
            total_score += eval_func(opp, player) 
    return total_score
'''
assert evaluate_round(O_ROCK, P_PAPER) == 8 
assert evaluate_round(O_PAPER, P_ROCK) == 1 
assert evaluate_round(O_SCISS, P_SCISS) == 6
'''

'''
assert evaluate_strag(O_ROCK, DRAW) == 4 
assert evaluate_strag(O_PAPER, LOSS) == 1 
assert evaluate_strag(O_SCISS, WIN) == 7
'''
total_score = read_and_eval('day2.txt', evaluate_strag)
print(total_score)
