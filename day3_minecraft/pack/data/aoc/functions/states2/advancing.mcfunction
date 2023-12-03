## State 0: Advancing
# Does nothing. If we encounter a gear, switch to state 1.

execute if block ~ ~ ~ #aoc:gear run scoreboard players set $State2 x 1
# immediately try the other state
execute if block ~ ~ ~ #aoc:gear run function aoc:states2/branch