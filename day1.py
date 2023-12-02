def part1(filename):
  sum = 0
  with open(filename, 'r') as input:
    for line in input:
      first_number = -1;
      second_number = -1;
      for char in line:
        if char >= '0' and char <= '9':
          first_number = int(char)
          break
      line = reversed(line)
      for char in line:
        if char >= '0' and char <= '9':
          second_number = int(char)
          break
      sum += first_number*10 + second_number
  return sum

print(part1('input1'))
print(part1('task1'))

      