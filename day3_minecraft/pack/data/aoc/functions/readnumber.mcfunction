## readnumber
## @as @at cursor position
# Read a number into the $ReadNum variable.

scoreboard players set $ReadNum x 0
summon minecraft:marker ~ ~ ~ {Tags:["aoc_readnumber"]}
execute as @e[type=marker,tag=aoc_readnumber] at @s run function aoc:readnumber/seek
execute as @e[type=marker,tag=aoc_readnumber] at @s run tp @s ~1 ~ ~
execute as @e[type=marker,tag=aoc_readnumber] at @s run function aoc:readnumber/read
kill @e[type=marker, tag=aoc_readnumber]
