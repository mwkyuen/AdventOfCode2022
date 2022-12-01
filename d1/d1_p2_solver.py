with open('./d1_input.txt', 'r') as input:
    lines = input.readlines()
    total_calories = 0
    elves = []
    for line in lines:
        val = line.strip()
        if not val:
            elves.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(val)
    sorted_elves = sorted(elves, reverse=True)
    print(sum(sorted_elves[:3]))
