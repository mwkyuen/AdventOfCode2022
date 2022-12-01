with open('./d1_input.txt', 'r') as input:
    lines = input.readlines()
    total_calories = 0
    max_elf = 0
    for line in lines:
        val = line.strip()
        if not val:
            if max_elf <= total_calories:
                max_elf = total_calories
            total_calories = 0
        else:
            total_calories += int(val)
    print(total_calories)
    print(max_elf)
