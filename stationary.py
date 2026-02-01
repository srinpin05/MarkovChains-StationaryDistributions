import numpy as np
#transition dynamics of a random markov chain
P = np.array([
    [0.5, 0.5, 0.0],
    [0.0, 0.5, 0.5],
    [0.5, 0.0, 0.5]
])

#initial distribution
pi = np.array([0.20, 0.60, 0.20])

for i in range(100):
    if i%10 == 0:
        print(pi)
    else:
        pi = pi @ P
# Above was purely mathematical no experiences.
# Lets verify using simulation now
print("\n")
state = 0
counts = np.zeros(3)
for i in range(10000):
    counts[state] +=1
    state = np.random.choice(3, p=P[state])

print(f"Simulation Results: {counts}")