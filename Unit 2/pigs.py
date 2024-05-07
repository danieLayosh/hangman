input_number = input("Please enter a three digit number: ")

bricks = int(input_number)

first_pig = bricks % 10

second_pig = (bricks / 10) % 10

theard_pig = ((bricks / 10) / 10) % 10

total_bricks = int(first_pig + second_pig + theard_pig)

print('sum:', total_bricks)

bricks_per_pig = total_bricks // 3

print("brickes per pig: ", bricks_per_pig)

rem = total_bricks % 3

print("rem: ", rem)

divides_evenly = rem == 0

print(divides_evenly)
