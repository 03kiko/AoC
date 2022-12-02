def score(input):
    score=0
    for round in input:
        if round[2]=='Y':
            score+=3
            if round[0]=='A': 
                score+=1
            elif round[0]=='B':
                score+=2
            else:
                score+=3
        elif round[2]=='Z':
            score+=6
            if round[0]=='A':
                score+=2
            elif round[0]=='B':
                score+=3
            else: 
                score+=1
        else:
            if round[0]=='A':
                score+=3
            elif round[0]=='B':
                score+=1
            else:
                score+=2
    return score

print(score(open('input.txt','r')))