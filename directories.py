from pathlib import Path

path = Path()
for file in path.glob('*.*'):
    print(file)

for file in path.glob('*'):
    print(file)