# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# game_map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = int(input("Where do you want to put the treasure? "))
# row = position // 10 - 1
# col = position % 10 - 1 

# game_map[row][col] = "X"

# print(f"{row1}\n{row2}\n{row3}")

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

