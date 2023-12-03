## State 3: Exit Number
# invoke the number-collection routine.
# go back to state 0.

execute if block ~1 ~ ~ #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~1 ~0.75 ~ 0 0 0 1 3 force
execute if block ~1 ~ ~1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~1 ~0.75 ~-1 0 0 0 1 3 force
execute if block ~1 ~ ~-1 #aoc:symbol run scoreboard players set $NumberIsValid x 1
particle dust 0.8 0.8 0.8 0.5 ~1 ~0.75 ~1 0 0 0 1 3 force
execute at @s run function aoc:readnumber
execute if score $NumberIsValid x matches 1 run scoreboard players operation $Total1 x += $ReadNum x
scoreboard players set $State x 0
# rest for a tick because we're technically still on a 'number' tile
