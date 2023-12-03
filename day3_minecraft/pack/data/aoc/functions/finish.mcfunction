scoreboard players set $RuntimeState x 0
execute if score $OutputState x matches ..-1 run tellraw @a {"text":"[!] An error occured!","color":"red","bold": true}
execute if score $OutputState x matches -1 run tellraw @a {"text":"Ran off the end of the data.","color":"red"}
execute if score $OutputState x matches -1 run tellraw @a {"text":"Check that the EOL and EOF markers are correct.","color":"red"}
execute if score $OutputState x matches -1 run tellraw @a [{"text":"If you removed some blocks, try ","color":"red"},{"text":"reloading the ROM","color":"green","underlined":true,"clickEvent":{"action":"run_command","value":"/function aoc:rom"}},{"text":"."}]
execute if score $OutputState x matches 1.. run tellraw @a {"text":"Success!","color":"green"}

# ticks to H:M:S
scoreboard players operation $Seconds x = $Duration x
scoreboard players operation $Seconds x /= $20 CONST
scoreboard players operation $Minutes x = $Seconds x
scoreboard players operation $Minutes x /= $60 CONST
scoreboard players operation $Seconds x %= $60 CONST

tellraw @a [{"text":"Completed in ","color":"gray"},{"score":{"name":"$Minutes","objective":"x"},"color":"green"},{"text":" min ","color":"green"},{"score":{"name":"$Seconds","objective":"x"},"color":"aqua"},{"text":" sec ","color":"aqua"},{"text":"(at normal speed)"}]

scoreboard players reset $Hours x
scoreboard players reset $Minutes x
scoreboard players reset $Seconds x

tellraw @a [{"text":"Part 1: ","color":"blue"},{"score":{"name":"$Total1","objective":"x"},"color":"aqua","italic":true}]
tellraw @a [{"text":"Part 2: ","color":"dark_purple"},{"score":{"name":"$Total2","objective":"x"},"color":"light_purple","italic":true}]
