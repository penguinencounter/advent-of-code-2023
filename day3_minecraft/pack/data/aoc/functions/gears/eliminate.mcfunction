execute if entity @s[tag=aoc_invalid] run return 0
tag @s add aoc_imm
tag @e[tag=aoc_gear_permute, tag=!aoc_imm, distance=..0.5] add aoc_invalid
tag @s remove aoc_imm
