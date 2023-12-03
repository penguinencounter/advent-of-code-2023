kill @e[tag=debug_cursor]
summon marker 0 16.5 0 {Tags:["debug_cursor"]}
function aoc:run_setup
scoreboard players set $RuntimeState x 1
scoreboard players set $Duration x 0
