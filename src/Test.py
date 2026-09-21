from src.statevector import statevector

s = statevector(1)
counts = [0, 0]
for i in range(0, 1000):
    counts[s.measure()] += 1

print(f"0 count: {counts[0]}\t1 count: {counts[1]}")