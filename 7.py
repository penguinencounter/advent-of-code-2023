from collections import defaultdict
with open('7.in') as f:
    d = f.read().splitlines()


def rank(hand: str):
    hand, bid = hand.split()
    strength = -1  # uhj

    histogram = defaultdict(int)
    histogram['J'] = 0
    for char in hand:
        if char == 'J': continue
        histogram[char] += 1

    names = "AKQT98765432J"
    maps = {}
    for i, name in enumerate(names):
        maps[name] = len(names) - i

    card_strn = tuple(map(lambda x: maps[x], hand))
    total_jokers = sum(map(lambda x: x == 'J', hand))

    # can we make 5ofac
    total_matching = max(histogram.values())
    if total_matching + total_jokers == 5:
        strength = 6
        return strength, *card_strn

    # four?
    if total_matching + total_jokers == 4:
        strength = 5
        return strength, *card_strn

    # full house?
    # there is <2 jokers here
    # it's a two pair effectively...
    if len(list(filter(lambda x: x == 2, histogram.values()))) == 2 and total_jokers > 0:
        strength = 4
        return strength, *card_strn
    if len(list(filter(lambda x: x == 3, histogram.values()))) == 1 and len(list(filter(lambda x: x == 2, histogram.values()))) == 1:
        strength = 4
        return strength, *card_strn

    if total_matching + total_jokers == 3:
        strength = 3
        return strength, *card_strn

    if len(list(filter(lambda x: x == 2, histogram.values()))) == 2:
        strength = 2
        return strength, *card_strn

    if len(list(filter(lambda x: x == 2, histogram.values()))) == 1 or total_jokers > 0:
        strength = 1
        return strength, *card_strn

    return strength, *card_strn


kvm = {}
for l in d:
    ranking_tupl = rank(l)
    print(l, ranking_tupl)
    kvm[l] = ranking_tupl

ranked = list(sorted(kvm.items(), key=lambda x: x[1]))
total = 0
for i, card in enumerate(ranked):
    total += (i + 1) * int(card[0].split()[1])
print(total)
