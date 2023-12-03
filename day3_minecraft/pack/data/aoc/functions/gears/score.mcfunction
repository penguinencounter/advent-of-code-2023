scoreboard players add $MatchIndex x 1
execute at @s run function aoc:readnumber

execute if score $MatchIndex x matches 1 run scoreboard players operation $Cog1 x = $ReadNum x
execute if score $MatchIndex x matches 2 run scoreboard players operation $Cog2 x = $ReadNum x
