import re
def assignment_pairs(input):
    pairs_overlapping=0
    for pairs in input:
        pairs_limits=re.findall('\d+',pairs) #\d+ finds ocorrunces of one or more digits
        first_elf=[]
        second_elf=[]
        for i in range(int(pairs_limits[0]),int(pairs_limits[1])+1):
            first_elf.append(i)
        for i in range(int(pairs_limits[2]),int(pairs_limits[3])+1):
            second_elf.append(i)
        for section in first_elf:
            if section in second_elf:
                pairs_overlapping+=1
                break
    return pairs_overlapping

print(assignment_pairs(open('input.txt','r')))