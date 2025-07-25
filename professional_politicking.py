import random
import time

# if you are contributing, please don't actually make this terribly political
# keep it lighthearted but you can make some jokes here and there

nations = []
parties = []
platforms = []

with open("config/nations.txt", "r") as file:
    for nation in file:
        nations.append(nation.strip())

with open("config/parties.txt", "r") as file:
    for party in file:
        parties.append(party.strip())

with open("config/platforms.txt", "r") as file:
    for platform in file:
        platforms.append(platform.strip())

ANSI_ESCAPE = {
    "YELLOW_BOLD": "\033[1;33m",
    "RESET": "\033[0m"
}


if __name__ == "__main__":
    print("Initalizing 'Professional Politicking' Round.")

    print('''
  ____  ____   ___  _____ _____ ____ ____ ___ ___  _   _    _    _       ____   ___  _     ___ _____ ___ ____ _  _____ _   _  ____ 
 |  _ \|  _ \ / _ \|  ___| ____/ ___/ ___|_ _/ _ \| \ | |  / \  | |     |  _ \ / _ \| |   |_ _|_   _|_ _/ ___| |/ /_ _| \ | |/ ___|
 | |_) | |_) | | | | |_  |  _| \___ \___ \| | | | |  \| | / _ \ | |     | |_) | | | | |    | |  | |  | | |   | ' / | ||  \| | |  _ 
 |  __/|  _ <| |_| |  _| | |___ ___) |__) | | |_| | |\  |/ ___ \| |___  |  __/| |_| | |___ | |  | |  | | |___| . \ | || |\  | |_| |
 |_|   |_| \_\\___/|_|   |_____|____/____/___\___/|_| \_/_/   \_\_____| |_|    \___/|_____|___| |_| |___\____|_|\_\___|_| \_|\____|
                                       
          ''')
    
    # add yourself if you contribute pls
    print("Contributors: Santiago Vega")

    candidates = []
    inputCandidates = True

    print(f"\n\n\n{ANSI_ESCAPE['YELLOW_BOLD']}Please make sure to have already selected candidates already!{ANSI_ESCAPE['RESET']}")
    print("EVENT ORGANIZER, you will be prompted to enter candidate names.")
    print("Type 'DONE' when you are done typing names.\n")

    while inputCandidates:
        inputted = input(f"Enter the name of candidate #{len(candidates)+1}: ")
        if inputted == "DONE":
            inputCandidates = False
            break
        candidates.append(inputted)

    randNation = random.randrange(0,len(nations))

    print("\n\n\nTo the great people of this room...")
    print(f"We need a president to represent the great nation of {ANSI_ESCAPE["YELLOW_BOLD"]}{nations[randNation]}{ANSI_ESCAPE["RESET"]}!")

    # ooh dramatic!!
    time.sleep(5)

    print("\nGenerating parties...")

    numOfParties = random.randint(2,len(candidates))

    selectedParties = {}
    randParties = random.sample(range(0,len(parties)), numOfParties)

    s = ["Pro-", "Anti-"]

    def randStance():
        return s[random.randint(0,1)]

    for n in randParties:
        randPlatform = random.sample(range(0,len(platforms)), 5)
        selectedParties[parties[n]] = f'''
        PLATFORM:
            \t1. {randStance()}{platforms[randPlatform[0]]}
            \t2. {randStance()}{platforms[randPlatform[1]]}
            \t3. {randStance()}{platforms[randPlatform[2]]}
            \t4. {randStance()}{platforms[randPlatform[3]]}
            \t5. {randStance()}{platforms[randPlatform[4]]}\n
        '''
    
    # pretend it's doing something
    time.sleep(2)

    print("\nYour parties this round will be...\n")
    for party in selectedParties:
        print(f"{ANSI_ESCAPE["YELLOW_BOLD"]}The {party} Party:{ANSI_ESCAPE["RESET"]}")
        print(selectedParties[party])

    time.sleep(7)

    takenParties = []

    if len(selectedParties) == len(candidates):
        for i, v in enumerate(selectedParties):
            print(f"{ANSI_ESCAPE["YELLOW_BOLD"]}{candidates[i]}{ANSI_ESCAPE['RESET']}, you will be running for {ANSI_ESCAPE["YELLOW_BOLD"]}the {v} Party{ANSI_ESCAPE['RESET']}!")
    else:
        for i, v in enumerate(candidates):
            # wack workaround
            # look im speedcoding this for rex okay
            parties_indexed = list(selectedParties.keys())
            randParty = random.randrange(0, len(selectedParties))

            takenParties.append(parties_indexed[randParty])

            print(f"{ANSI_ESCAPE["YELLOW_BOLD"]}{v}{ANSI_ESCAPE['RESET']}, you will be running for {ANSI_ESCAPE["YELLOW_BOLD"]}the {parties_indexed[randParty]} Party{ANSI_ESCAPE['RESET']}!")

            # pidgeonhole principle
            if (len(candidates)-(i+1))-len(takenParties) == 0:
                parties_indexed.remove(parties_indexed[randParty])


    print("\n\n\nThe game will now be directed by the EVENT ORGANIZERS.")

    

    