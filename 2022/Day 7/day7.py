def day7(input):
    import collections
    path=[]
    dir_size=collections.defaultdict(int)
    for line in input:
        line_tokens=line.strip().split() #NOICE
        if line_tokens[0]=='$':
            if line_tokens[1]=='cd':
                if line_tokens[2]=='/':
                    path=['/']
                elif line_tokens[2]=='..':
                    del path[-1] #use .pop
                else:
                    path.append(line_tokens[2])
            else: #line_tokens[1]=='ls'
                pass
        else:
            try:
                size=int(line_tokens[0])
                for i in range(0,len(path)): #with this dir_size['/'] gives the total value!
                    dir_size['/'.join(path[:i+1])]+=size
            except ValueError:
                pass

    disk_size=70000000
    unused_space_needed=30000000
    space_to_free=unused_space_needed-(disk_size-dir_size['/']) #needed - free space

    part2=min((s for s in dir_size.values() if s>=space_to_free)) #or sorted ..[0]
    part1=sum([s for s in dir_size.values() if s<=100000])
    
    return part1,part2


print(day7(open('input.txt','r')))