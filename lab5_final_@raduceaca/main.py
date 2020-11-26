from domain.parser import Parser

def show_menu():
    lr0 = Parser("data/g1.txt")

    print("\t1 : Terminals")
    print("\t2 : Non terminals")
    print("\t3 : Productions")
    print("\t4 : Productions for a given Non terminal")
    print("\t5 : Canonical collection")
    print("\n\t0 : exit")

    # menu = {
    #     "1": lambda: lr0.print_data(1),
    #     "2": lambda: lr0.print_data(2),
    #     "3": lambda: lr0.print_data(3),
    #     "4": lambda: lr0.print_production(input("Please give a non terminal:")),
    #     "5": lambda: lr0.canonical_collection(),
    #     "6": exit
    # }

    while True:
        run = input("$ ")

        if(run == "1"):
            print(lr0.get_non_terminals())
        elif(run == "2"):
            print(lr0.get_non_terminals())
        elif(run == "3"):
            print(lr0.get_productions())
        elif(run == "4"):
            nt = input("$ Non terminal: ")
            res = lr0.get_production(nt)

            if(res != None):
                for e in res:
                    print(e[0], "->", e[1])
            else:
                print("Given non terminal is wrong.")
        elif(run == '5'):
            lr0.canonical_collection()
        elif(run == '0'):
            exit()
        else:
            print("Wrong option")


if __name__ == '__main__':
    show_menu()
