tp @s ~-1 ~ ~
particle dust 0.5 1 0.5 0.75 ~ ~1.5 ~ 0 0 0 0.05 3 force
execute at @s if block ~ ~ ~ #aoc:digits run function aoc:readnumber/seek
