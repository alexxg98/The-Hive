#Fail-Safe function
def setScore(rep_score, new_score):
    rep_score = new_score
    return rep_score

#Set initial score and SU change score
def changeScore(rep_score, deltaScore):
    # an OU can give a score 0-10; a VIP can give score 0-20
    rep_score += deltaScore
    return rep_score

def tabooWord(rep_score, count):
    if count < 1:
        pass
    if count == 1:
        rep_score -= 1
    if count > 1:
        rep_score -=5
    return rep_score

def compliment(rep_score, count):
    # if count == 3:
    #     rep_score -= 1
    # if count > 1:
    #     rep_score -=5
    return rep_score

def complain(rep_score):
    return rep_score

def warning(rep_score, count):
    if count == 3:
        rep_score -= 5
    return rep_score

def kickout(rep_score):
    rep_score -= 10
    return rep_score
