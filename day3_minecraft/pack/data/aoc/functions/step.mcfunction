tp @s ~1 ~ ~
execute at @s if block ~ ~ ~ #aoc:eol run tp @s 0 ~ ~1
execute at @s if block ~ ~ ~ #aoc:eof run return 1
# the cursor got lost on the way to the gondola lift
# now it's out in the middle of nowhere
# send the emergency rescue mission!!
execute at @s unless block ~ ~ ~ #aoc:not_open_bus run return -1


execute at @s run function aoc:states1/branch
execute at @s run function aoc:states2/branch
return 0
