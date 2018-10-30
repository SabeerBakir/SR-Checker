from SR_Check import sr_get


def average(mylist):
    if len(mylist) is 0:
        return 0
    else:
        return sum(mylist)/len(mylist)


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


temp = 0
battletags = []
sr_num = []
unranked_num = 0
private_num = 0
unknown_num = 0

run = True
while run:
    print("1) Enter text file with battletags? ?")
    print("2) Enter battletags manually ? ")
    try:
        choice = int(input("Input: "))
        if choice is 1:
            filename = input("Enter file name: ")
            try:
                file = open(filename, "r")
                total_battletags = file_len(filename)
                for line in file:
                    line = line.strip()
                    sr = sr_get(line)
                    if not (sr <= 0):
                        print(str(line) + ": " + str(sr))
                        sr_num.append(sr)
                    if sr is 0:
                        private_num += 1
                    elif sr is -1:
                        unknown_num += 1
                    elif sr is -2:
                        unranked_num += 1

                print()
                print("Average SR: " + str(round(average(sr_num))))
                print("Total Battletags: " + str(total_battletags))
                print("Confirmed Placed Accounts: " + str(total_battletags - private_num - unranked_num - unknown_num))
                print("Private Accounts: " + str(private_num))
                print("Unranked Accounts: " + str(unranked_num))
                print("Unknown Battletags: " + str(unknown_num))
                print()
                input("Press any key...")
                run = False
                exit()
            except FileNotFoundError:
                print("File Does Not Exist")
                input("Press any key...")
                run = False
                exit()
        elif choice is 2:
            print("Battletags are case sensitive. Press Enter when finished")
            print("Example: Player-12345")
            print()
            while temp is 0:
                battletag = input("Enter battletag: ")
                if len(battletag) is not 0:
                    battletags.append(battletag)
                else:
                    temp = 1

            total_battletags = len(battletags)
            for battletag in battletags:
                sr = sr_get(battletag)
                if not (sr <= 0):
                    print(str(battletag) + ": " + str(sr))
                    sr_num.append(sr)
                if sr is 0:
                    private_num += 1
                elif sr is -1:
                    unknown_num += 1
                elif sr is -2:
                    unranked_num += 1

            print()
            print("Average SR: " + str(round(average(sr_num))))
            print("Total Battletags: " + str(total_battletags))
            print("Confirmed Placed Accounts: " + str(total_battletags - private_num - unranked_num - unknown_num))
            print("Private Accounts: " + str(private_num))
            print("Unranked Accounts: " + str(unranked_num))
            print("Unknown Battletags: " + str(unknown_num))
            print()
            input("Press any key...")
            run = False
            exit()
        else:
            print("Invalid Option")
    except ValueError:
        print("Please Enter Integer Values Only")
