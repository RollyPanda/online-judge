def last2(s):
  a = 0
  for i in range(len(s) - 2):
    if s[i: i + 2] == s[-2:]:
      a += 1
  return a
if __name__ == '__main__':
  s = input()
  print(last2(s))
