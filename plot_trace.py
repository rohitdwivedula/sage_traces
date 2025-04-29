import sys
import matplotlib.pyplot as plt
from collections import Counter

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    nums = [int(line.strip()) for line in f]

freq = Counter(nums)

x = sorted(freq)
y = [freq[n] * 12 for n in x]
plt.plot(x, y, marker='x')
plt.xlabel("Time (num)")
plt.ylabel("Bandwidth (frequency)")
plt.title("Frequency vs Number")
plt.grid(True)
plt.show()