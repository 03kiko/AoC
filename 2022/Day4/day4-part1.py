import re
def assignment_pairs(input):
    pairs_fully_contained_in_the_other=0
    for pairs in input:
        pairs_limits=re.findall('\d+',pairs) #\d+ finds ocorrunces of one or more digits
        first_elf=[]
        second_elf=[]
        for i in range(int(pairs_limits[0]),int(pairs_limits[1])+1):
            first_elf.append(i)
        for i in range(int(pairs_limits[2]),int(pairs_limits[3])+1):
            second_elf.append(i)
        contains=(all(id in first_elf for id in second_elf) or 
                  all(id in second_elf for id in first_elf))
        # Checks if all ids of the first elf are fully coitained by the second elf
        # and vice-versa.
        if contains:
            pairs_fully_contained_in_the_other+=1
    return pairs_fully_contained_in_the_other

print(assignment_pairs(open('input.txt','r')))