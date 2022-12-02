def score(input):
    score=0
    for round in input:
        if (round[0]=='A' and round[2]=='Y') or (round[0]=='B' and round[2]=='Z') or (round[0]=='C' and round[2]=='X'):
            score+=6
        elif (round[0]=='A' and round[2]=='X') or (round[0]=='B' and round[2]=='Y')or(round[0]=='C' and round[2]=='Z'):
            score+=3
        if round[2]=='X':
            score+=1
        elif round[2]=='Y':
            score+=2
        else:
            score+=3
    return score

print(score(open('input.txt','r')))