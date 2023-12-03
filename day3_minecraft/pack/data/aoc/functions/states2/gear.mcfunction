summon marker ~1 ~ ~1 {Tags:["aoc_gear_permute"]}
summon marker ~ ~ ~1 {Tags:["aoc_gear_permute"]}
summon marker ~-1 ~ ~1 {Tags:["aoc_gear_permute"]}
summon marker ~-1 ~ ~ {Tags:["aoc_gear_permute"]}
summon marker ~-1 ~ ~-1 {Tags:["aoc_gear_permute"]}
summon marker ~ ~ ~-1 {Tags:["aoc_gear_permute"]}
summon marker ~1 ~ ~-1 {Tags:["aoc_gear_permute"]}
summon marker ~1 ~ ~ {Tags:["aoc_gear_permute"]}

execute as @e[tag=aoc_gear_permute] at @s run function aoc:gears/slide1

execute as @e[tag=aoc_gear_permute] at @s run function aoc:gears/eliminate
kill @e[tag=aoc_invalid]

execute store result score $MatchCount x if entity @e[tag=aoc_gear_permute]
scoreboard players set $MatchIndex x 0
execute if score $MatchCount x matches 2 as @e[tag=aoc_gear_permute] at @s run function aoc:gears/score
# tellraw @a [{"text": "i see "}, {"score": {"name": "$TEMP_a", "objective": "x"}, "color": "red"}, {"text": " adjacent numbers"}]
execute if score $MatchCount x matches 2 run scoreboard players operation $Cog1 x *= $Cog2 x
execute if score $MatchCount x matches 2 run scoreboard players operation $Total2 x += $Cog1 x

kill @e[tag=aoc_gear_permute]
scoreboard players set $State2 x 0