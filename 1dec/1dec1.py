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





def main():
    val_list = gen_list()
    print(max(val_list))
    return 0

if __name__ == "__main__":
    main()