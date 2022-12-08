field = []
with open('input') as f:
    for line in f:
        field.append(line.strip())

height = len(field)
width = len(field[0])


# issue 1
total = height * 2 + width * 2 - 4
for col in range(1, width - 1):
    for row in range(1, height - 1):
        visible = False

        # check left
        for i in range(col):
            if field[row][i] >= field[row][col]:
                break
        else:
            visible = True
        
        if not visible:
            # check right
            for i in range(width - 1, col, -1):
                if field[row][i] >= field[row][col]:
                    break
            else:
                visible = True

        if not visible:
            #check top
            for i in range(row):
                if field[i][col] >= field[row][col]:
                    break
            else:
                visible = True

        if not visible:
            # check bottom
            for i in range(height - 1, row, - 1):
                if field[i][col] >= field[row][col]:
                    break
            else:
                visible = True

        if visible:
            total += 1

print(f'issue 1: {total=}')

# issue 2
max_score = 0
for col in range(1, width - 1):
    for row in range(1, height - 1):
        score = 1

        # check left
        count = 0
        for i in range(col - 1, -1, -1):
            if field[row][i] < field[row][col]:
                count += 1
            else:
                count += 1
                break
        score *= count
        count = 0
        # check right
        for i in range(col + 1, width):
            if field[row][i] < field[row][col]:
                count += 1
            else:
                count += 1
                break
        score *= count
        count = 0
        #check top
        for i in range(row - 1, -1, -1):
            if field[i][col] < field[row][col]:
                count += 1
            else:
                count += 1
                break

        score *= count
        count = 0
        # check bottom
        for i in range(row + 1, height):
            if field[i][col] < field[row][col]:
                count += 1
            else:
                count += 1
                break
        
        score *= count
        if score > max_score:
            max_score = score

print(f'issue 2: {max_score=}')
