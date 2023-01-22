data = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_putted_out = []
for cell in data:
    fire_type = cell.split(" = ")[0]
    value = int(cell.split(" = ")[1])
    needed_water = 0
    if fire_type == "High" and 81 <= value <= 125:
        needed_water = value
    elif fire_type == "Medium" and 51 <= value <= 80:
        needed_water = value
    elif fire_type == "Low" and 1 <= value <= 50:
        needed_water = value
    if needed_water == 0:
        continue
    if water - needed_water <= 0:
        break
    cells_putted_out.append(value)
    effort += value * 0.25
    water -= needed_water
    total_fire += needed_water
print(f"Cells:")
for cell in cells_putted_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")