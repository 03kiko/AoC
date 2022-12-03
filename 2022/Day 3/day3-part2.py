def sum_priorities(input):
    sum=0
    group=[]
    for rucksack in input:
        previous_items=[]
        group+=[list(rucksack)]
        if len(group)==3:                
            for item in group[0]:
                if item in group[1] and item not in previous_items and item != '\n':
                    if item in group[2]:
                        if ord('A')<=ord(item)<=ord('Z'):
                                sum+=27+ord(item)-ord('A')
                        else:
                            sum+=ord(item)-ord('a')+1  
                previous_items+=item
            group=[]
    return sum
print(sum_priorities(open('input.txt','r')))