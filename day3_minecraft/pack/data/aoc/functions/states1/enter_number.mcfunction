## State 1: Enter number
# Immediately switches to state 2 and runs it.

scoreboard players set $NumberIsValid x 0
execute if block ~-1 ~ ~ #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~-1 ~0.75 ~ 0 0 0 1 3 force
execute if block ~-1 ~ ~1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~-1 ~0.75 ~1 0 0 0 1 3 force
execute if block ~-1 ~ ~-1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~-1 ~0.75 ~-1 0 0 0 1 3 force
scoreboard players set $State x 2
function aoc:states1/branch
