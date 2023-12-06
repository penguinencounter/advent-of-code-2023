# put your ACTUAL input in here...
times = []
dists = []

def bf(t, d):
    counter = 0
    for x in range(t):
        score = x * (t - x)
        if score > d:
            counter += 1
    return counter


prod = 1
for k, v in zip(times, dists):
    prod *= bf(k, v)
print(prod)

print(bf(int(''.join(map(str, times))), int(''.join(map(str, dists)))))