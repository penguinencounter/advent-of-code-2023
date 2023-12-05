from collections import defaultdict


with open("3.in") as f:
    data = f.read()

kv = {
    "0": "minecraft:red_concrete",
    "1": "minecraft:orange_concrete",
    "2": "minecraft:yellow_concrete",
    "3": "minecraft:lime_concrete",
    "4": "minecraft:green_concrete",
    "5": "minecraft:cyan_concrete",
    "6": "minecraft:light_blue_concrete",
    "7": "minecraft:blue_concrete",
    "8": "minecraft:purple_concrete",
    "9": "minecraft:magenta_concrete",
    ".": "minecraft:black_stained_glass",
    "*": "minecraft:diamond_block",
}
symbol_default = "minecraft:amethyst_block"
eol = "minecraft:acacia_planks"
eof = "minecraft:red_glazed_terracotta"

histogram = defaultdict(int)

with open("rom.mcfunction", "w") as f:
    for ci, col in enumerate(data.splitlines()):
        if col.strip() == "":
            continue
        for ri, chr in enumerate(col):
            block = kv[chr] if chr in kv else symbol_default
            histogram[block] += 1
            f.write(f"setblock {ri} 16 {ci} {block}\n")
        f.write(f"setblock {ri+1} 16 {ci} {eol}\n")
    f.write(f"setblock 0 16 {ci+1} {eof}\n")

print(f"all done! -> rom.mcfunction")
print(f"stats:")
header1 = "Namespaced ID"
header2 = "Count"
keys = list(histogram.keys()) + [header1]
values = list(map(str, histogram.values())) + [header2]
column1 = max(map(len, keys))
column2 = max(map(len, values))
print(f"{header1.ljust(column1)} | {header2.ljust(column2)}")
print("=" * (column1 + column2 + 3))

for k, v in histogram.items():
    print(f"{str(k).ljust(column1)} | {str(v).ljust(column2)}")
