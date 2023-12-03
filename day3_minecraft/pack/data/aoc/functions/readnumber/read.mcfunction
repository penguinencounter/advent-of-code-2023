execute unless block ~ ~ ~ #aoc:digits run return 0

# shift the digits over to the left one...
scoreboard players operation $ReadNum x *= $10 CONST
# add the next digit
execute if block ~ ~ ~ #aoc:digit_1 run scoreboard players add $ReadNum x 1
execute if block ~ ~ ~ #aoc:digit_2 run scoreboard players add $ReadNum x 2
execute if block ~ ~ ~ #aoc:digit_3 run scoreboard players add $ReadNum x 3
execute if block ~ ~ ~ #aoc:digit_4 run scoreboard players add $ReadNum x 4
execute if block ~ ~ ~ #aoc:digit_5 run scoreboard players add $ReadNum x 5
execute if block ~ ~ ~ #aoc:digit_6 run scoreboard players add $ReadNum x 6
execute if block ~ ~ ~ #aoc:digit_7 run scoreboard players add $ReadNum x 7
execute if block ~ ~ ~ #aoc:digit_8 run scoreboard players add $ReadNum x 8
execute if block ~ ~ ~ #aoc:digit_9 run scoreboard players add $ReadNum x 9

# move the cursor to the right
tp @s ~1 ~ ~
execute at @s run function aoc:readnumber/read
