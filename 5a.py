import re
from typing import Optional

with open("5.in") as f:
    m = f.read()
    d = m.splitlines()


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

    def overlap2(self, above: "mapper") -> Optional["mapper"]:
        alpha = max(self.inL, above.outL) - self.inL
        beta = min(self.inR, above.outR) - self.inR
        if abs(alpha) > self.inputArea or abs(beta) > self.inputArea:
            return None
        return mapper(
            self.inL + alpha, self.inR + beta, self.outL + alpha, self.outR + beta
        )

    def apply(self, below: "mapper") -> Optional["mapper"]:
        their_persp = below.overlap2(self)
        if their_persp is None:
            return None
        our_persp = self.overlap(below)
        if our_persp is None:
            return None
        return mapper(our_persp.inL, our_persp.inR, their_persp.outL, their_persp.outR)

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

    def subtract2(self, below: "mapper") -> list["mapper"]:
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

    def direct(self) -> "mapper":
        return mapper(self.inL, self.inR, self.inL, self.inR)

    def __hash__(self):
        return hash((self.inL, self.inR, self.outL, self.outR))

    @classmethod
    def from_range(cls, target: range) -> "mapper":
        return mapper(target.start, target.stop, target.start, target.stop)

    def __repr__(self):
        return (
            f"<{self.inL}, {self.inR} ({self.inputArea}) -> {self.outL}, {self.outR}>"
        )


seeds = list(map(int, re.findall(r"\d+", d[0])))
ranges = []
for idx in range(0, len(seeds), 2):
    ranges.append(range(seeds[idx], seeds[idx] + seeds[idx + 1]))

sets = list(map(mapper.from_range, ranges))


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

# see 'sets' above...
up_next = []
for mapset in maps:
    print(sets)
    for source_range in sets:
        fragmentation = {source_range}
        for map_ in mapset:
            if (overlap := source_range.apply(map_)) is not None:
                up_next.append(overlap)
            fragmentation = [x.subtract2(map_) for x in fragmentation]
            fragmentation = {
                i2 for i1 in fragmentation for i2 in i1 if i2.inputArea > 0
            }
        up_next.extend(fragmentation)
    sets = up_next.copy()
    up_next.clear()


print(list(sorted(sets, key=lambda x: x.outL)))
