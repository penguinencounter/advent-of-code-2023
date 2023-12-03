execute if score $RuntimeState x matches 1 run scoreboard players add $Duration x 1
execute if score $RuntimeState x matches 1 store result score $OutputState x as @e[tag=debug_cursor] at @s run function aoc:step
execute if score $RuntimeState x matches 1 unless score $OutputState x matches 0 run function aoc:finish

