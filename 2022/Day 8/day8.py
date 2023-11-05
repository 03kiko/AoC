def day_8(input):
    def isvisible(grid,r,c):
        if c==0 or c==column-1 or r==0 or r==row-1:
            return 1
        #left
        if all(grid[r][c1]<grid[r][c] for c1 in range(c)):
            return 1
        #right
        if all(grid[r][c1]<grid[r][c] for c1 in range(c+1,column)):
            return 1
        #up
        if all(grid[r1][c]<grid[r][c] for r1 in range(r)):
            return 1
        #down
        if all(grid[r1][c]<grid[r][c] for r1 in range(r+1,row)):
            return 1
        return 0
        
    def scenic_score(grid,r,c):
        if c==0 or c==column-1 or r==0 or r==row-1:
            return 0
        #left
        for  c1 in range(1,c+1):
            if grid[r][c-c1]>=grid[r][c]:
                break
        left=c1
        #right
        for c2 in range(1,column-c):
            if grid[r][c+c2]>=grid[r][c]:
                break
        right=c2
        for r1 in range(1,r+1):
            if grid[r-r1][c]>=grid[r][c]:
                break
        up=r1
        for r2 in range(1,row-r):
            if grid[r+r2][c]>=grid[r][c]:
                break
        down=r2
        return up*down*right*left
    grid=[list(map(int,line.strip())) for line in input] #!!!
    
    part1=0
    part2=0

    row=len(grid)
    column=len(grid[0])

    for r in range(row):
        for c in range(column):
            part1+=isvisible(grid,r,c)
            part2=max(part2,scenic_score(grid,r,c))

    return part1,part2

print(day_8(open('input.txt','r')))