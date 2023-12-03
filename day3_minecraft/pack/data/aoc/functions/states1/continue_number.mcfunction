## State 2: Continue Number

execute if block ~ ~ ~1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~ ~0.75 ~1 0 0 0 1 3 force
execute if block ~ ~ ~-1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~ ~0.75 ~-1 0 0 0 1 3 force
# read ahead
execute unless block ~1 ~ ~ #aoc:digits run scoreboard players set $State x 3
execute unless block ~1 ~ ~ #aoc:digits run function aoc:states1/branch
