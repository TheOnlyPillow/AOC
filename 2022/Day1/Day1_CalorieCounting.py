elves = {}

with open("ElfInput.txt","r") as inventory:
    inventory_data = inventory.read()
    
max_cal_elve = 0
for elve_num, snacks in enumerate(inventory_data.split("\n\n")):
    elve_cal_total = 0
    for snack_cal in snacks.split("\n"):
        if snack_cal.isnumeric():
            elve_cal_total += int(snack_cal)
    elves[elve_num] = elve_cal_total
elves = sorted(elves.values(),reverse=True)
top_elf = elves[0]
print(top_elf)
top_three_elves_total = sum([elves[0],elves[1],elves[2]])
print(top_three_elves_total)


# print(f"{max_cal_elve} {elves[max_cal_elve]}")
    