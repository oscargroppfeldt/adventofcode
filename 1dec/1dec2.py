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




foodlist = open("list.txt")
print(foodlist)


def main_2(lista):
    second_elf = 0
    third_elf = 0
    index = 0
    max_index = 0
    total = 0
    elf = []
    max_elf = 0
    for i in lista:
        if i == '\n':
            index += 1
            total = sum(elf)
            elf = []
            if total > max_elf:
                max_elf = total
                print(max_elf)
                max_index = index 
                elf = []
                continue
                
            if total > second_elf:
                second_elf = total
                elf = []
                continue
                
            if total > third_elf:
                third_elf = total
                elf = []
                
        else:
            i = int(i)
            elf.append(i)
    total_three = max_elf+second_elf+third_elf
    return print(f"Alv nummer {max_index} har {max_elf} kalorier vilket är flest av alla. Top tre alver har totalt {total_three}")


print(main_2(foodlist))