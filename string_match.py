def string_match(a, b):
  min_len = min(len(a), len(b))
  t = 0
  for i in range(min_len - 1):
    if a[i:i + 2] == b[i:i + 2]:
      t += 1
  return t
if __name__ == '__main__':
  a, b = input().split(', ')
  print(string_match(a, b))
