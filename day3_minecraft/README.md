# Day 3 in Minecraft

Continuing with doing weird things with games...

1. Create `3.in` in the CWD and run `generate.py`
2. Move the generated `rom.mcfunction` to this location:

```
pack/data/aoc/functions/rom.mcfunction
```

3. Create a new creative superflat Minecraft world with cheats enabled in 1.20.1 or later.
4. On the world creation screen, switch to the **More** tab and click 'Data Packs'.
5. Drag the pack folder from your system file manager into the game window.
6. Click **Yes**, hover the `Advent of Code 2023` pack on the left and click the arrow to move it to the right, and press **Done**.
7. Create the world.
8. Run `/function aoc:rom` in the chat box.
9. Fly up to the generated platform.
10. Run `/function aoc:run`.
11. (Optional) do `/scoreboard objectives setdisplay sidebar x` to show the variables on the right side as the program runs.
12. Wait ~16 minutes 20 seconds
13. Solve day 3
