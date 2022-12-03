def sum_priorities(input):
    sum=0
    for rucksack in input:
        previous_items=[]
        rucksack_compartments=[]    
        size_compartment=int((len(rucksack)-1)/2)
        rucksack_compartments+=[rucksack[:size_compartment]],list(rucksack[size_compartment:])
        for item in rucksack_compartments[0][0]:
            if item in rucksack_compartments[1] and item not in previous_items:
                if ord('A')<=ord(item)<=ord('Z'):
                        sum+=27+ord(item)-ord('A')
                else:
                    sum+=ord(item)-ord('a')+1
            previous_items+=item
    return sum
print(sum_priorities(open('input.txt','r')))