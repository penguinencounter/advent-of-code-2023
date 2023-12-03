execute unless block ~ ~ ~ #aoc:digits run particle dust 1 0.5 0.5 0.75 ~ ~1.25 ~ 0 0 0 1 3 force
execute unless block ~ ~ ~ #aoc:digits run kill @s
execute unless block ~ ~ ~ #aoc:digits run return 0
particle dust 1 1 0.5 0.75 ~ ~1.25 ~ 0 0 0 1 3 force

execute at @s run function aoc:readnumber/seek
execute at @s run tp @s ~1 ~ ~
execute at @s run particle dust 0.5 1 1 0.75 ~ ~2 ~ 0 0 0 0.05 3 force
