import re
from typing import Optional

with open("5.in") as f:
    m = f.read()
    d = m.splitlines()

seeds = list(map(int, re.findall(r"\d+", d[0])))
inputspace_size = 0
for k in range(0, len(seeds), 2):
    inputspace_size += seeds[1]
print(inputspace_size)


class mapper:
    def __init__(self, inL, inR, outL, outR):
        self.outL = outL
        self.inR = inR
        self.inL = inL
        self.outR = outR

    def of(self, val):
        if val >= self.inR or val <= self.inL:
            return False, 0
        index_of_input = val - self.inL
        return True, self.outL + index_of_input

    @property
    def inputArea(self):
        return self.inR - self.inL

    def overlap(self, below: "mapper") -> Optional["mapper"]:
        alpha = max(self.outL, below.inL) - self.outL
        beta = min(self.outR, below.inR) - self.outR
        ourWidth = self.outR - self.outL
        if abs(alpha) > ourWidth or abs(beta) > ourWidth:
            return None  # no overlap.

        return mapper(
            self.inL + alpha, self.inR + beta, self.outL + alpha, self.outR + beta
        )

    def subtract(self, above: "mapper") -> list["mapper"]:
        if above.outL >= self.inR:
            return [self]
        if above.outR < self.inL:
            return [self]
        alpha = max(self.inL, above.outL) - self.inL
        beta = min(self.inR, above.outR) - self.inR
        if alpha == 0:
            return [
                mapper(
                    self.inL + (self.inputArea + beta),
                    self.inR,
                    self.outL + (self.inputArea + beta),
                    self.outR,
                )
            ]
        if beta == 0:
            return [
                mapper(
                    self.inL,
                    self.inR - (self.inputArea - alpha),
                    self.outL,
                    self.outR - (self.inputArea - alpha),
                )
            ]
        left_side = mapper(self.inL, self.inL + alpha, self.outL, self.outL + alpha)
        right_side = mapper(self.inR + beta, self.inR, self.outR + beta, self.outR)
        return [left_side, right_side]

    def subtract2(self, below: 'mapper') -> list['mapper']:
        if below.inL >= self.outR:
            return [self]
        if below.inR < self.outL:
            return [self]
        alpha = max(self.outL, below.inL) - self.outL
        beta = min(self.outR, below.inR) - self.outR
        if alpha == 0:
            return [
                mapper(
                    self.inL + (self.inputArea + beta),
                    self.inR,
                    self.outL + (self.inputArea + beta),
                    self.outR
                )
            ]
        if beta == 0:
            return [
                mapper(
                    self.inL,
                    self.inR - (self.inputArea - alpha),
                    self.outL,
                    self.outR - (self.inputArea - alpha)
                )
            ]
        left_side = mapper(self.inL, self.inL + alpha, self.outL, self.outL + alpha)
        right_side = mapper(self.inR + beta, self.inR, self.outR + beta, self.outR)
        return [left_side, right_side]

    def direct(self) -> 'mapper':
        return mapper(self.inL, self.inR, self.inL, self.inR)

    def __repr__(self):
        return (
            f"<{self.inL}, {self.inR} ({self.inputArea}) -> {self.outL}, {self.outR}>"
        )


def parse_map(lines: list[str]) -> list[mapper]:
    ms = []
    for line in lines:
        if line.strip() == "":
            break
        b, a, c = list(map(int, line.split()))
        ms.append(mapper(a, a + c, b, b + c))
    return ms


testA = mapper(0, 50, 100, 150)
testB = mapper(110, 140, 0, 50)
print("subtraction result", testA.subtract2(testB))
print("transformed", list(map(mapper.direct, testA.subtract2(testB))))

print(seeds)
groups = m.split("\n\n")
maps = []

for group in groups:
    l = group.splitlines()
    if l[0].endswith("map:"):
        n = parse_map(l[1:])
        maps.append(n)

maps = list(reversed(maps))
# for mapset in maps[0]:
lowest = sorted(maps[0], key=lambda x: x.outL)[0]
print(f'targetting {lowest}')
fragments = [lowest]
next_up = []
maps = maps[1:]
for mapset in maps:
    while fragments:
        u = fragments.pop()
        leftovers = [u]
        for target in mapset:
            if (frag := target.overlap(u)) is not None:
                print('new fragment', frag)
                next_up.append(frag)
                leftovers = [partition.subtract(frag) for partition in leftovers]
                leftovers = [i2 for i1 in leftovers for i2 in i1]
                leftovers = list(filter(lambda x: x.inputArea > 0, leftovers))
        if len(leftovers) > 0:
            print(f'adding these: {list(map(mapper.direct, leftovers))}')
        next_up.extend(map(mapper.direct, leftovers))
    fragments = next_up.copy()
    next_up.clear()
    print(len(fragments), "fragments")

lowest2 = sorted(fragments, key=lambda x: x.outL)[0]
print(lowest2.inL, lowest2)

contestant = lowest2.inL
# run the gauntlet
for mapset in reversed(maps):
    for map_ in mapset:
        ok, val = map_.of(contestant)
        if ok:
            print(f'{contestant} -> {val}')
            contestant = val
            break
print(contestant)

# print(min(seeds))
