from os.path import abspath, expanduser, exists
from shutil import rmtree, copytree

target = "~/Documents/MinecraftInstances/1.20.1/.minecraft/saves/AOC2023/datapacks/pack"
at = abspath(expanduser(target))
print("target", at)
rmtree(at, ignore_errors=True)

sources = ["pack", "day3_minecraft/pack", "advent-of-code-2023/day3_minecraft/pack"]
for source in sources:
    if exists(source):
        copyfrom = source
        break
else:
    raise FileNotFoundError("i don't know where the pack files are")
print("source", copyfrom)
copytree(copyfrom, at, dirs_exist_ok=True)
print("done")
