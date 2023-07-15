
def main():
    provinces_list = read_list("provinces.txt")
    
    print(f"\n{provinces_list}")
    
    provinces_list.pop(0)
    provinces_list.pop(-1)
    
    print(f"\nprovinces list with the first and last provinces erased: \n {provinces_list}")

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    alberta_times = provinces_list.count("Alberta")

    print(f"\n {provinces_list}")
    print(f"\nAlberta appears {alberta_times} times in the updated list")




def read_list(provinces):

    text_list = []

    with open(provinces, "rt") as provinces_file:

        for line in provinces_file:

            clean_line = line.strip()
            text_list.append(clean_line)

        return text_list

if __name__ == "__main__":
    main()