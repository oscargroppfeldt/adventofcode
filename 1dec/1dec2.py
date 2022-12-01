def gen_list():
    elf_total_list = []
    with open("list.txt") as file:
        data = file.read()
        elf_list = data.split("\n\n")
        for elf in elf_list:
            food_item_list = elf.split("\n")
            elf_sum = 0
            for food in food_item_list:
                elf_sum += int(food)
            elf_total_list.append(elf_sum)
    return elf_total_list

def get_max_and_index(input_list):
    enum = list(enumerate(input_list))
    max_element = max(input_list)
    max_index = [index for (index,element) in enum if element == max_element]
    return max_index

def main():
    val_list = gen_list()
    val_list.sort()
    val_list.reverse()
    tot = val_list[0] + val_list[1] + val_list[2]
    print(tot)
    """
    total = 0
    for i in range(3):
        elf = get_max_and_index(val_list)
        if len(elf) == 1:
            total += val_list[elf[0]]
            del val_list[elf[0]]
            continue
        else
    """

    
    return 0

if __name__ == "__main__":
    main()
