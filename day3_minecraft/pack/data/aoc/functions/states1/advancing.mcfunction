## State 0: Advancing
# Does nothing. If we encounter a number, switch to reading the number.

execute if block ~ ~ ~ #aoc:digits run scoreboard players set $State x 1
# immediately try the other state
execute if block ~ ~ ~ #aoc:digits run function aoc:states1/branch