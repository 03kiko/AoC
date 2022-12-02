def most_cal(input):
    sum=0
    max=0
    for x in input:
        if x!='\n':
            sum+=int(x)
        elif max<sum:
            max=sum
            sum=0
        else:    
            sum=0
    return max
print(most_cal(open('input.txt','r')))