import sys

# Prints to standard output.
def findStartAndEndLocations(pairs):
  for line in pairs:



# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    pairs.append(line.split(" "))

  findStartAndEndLocations(pairs)

main()
