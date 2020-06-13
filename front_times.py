def front_times(s, n):
  return s[:3] * n

if __name__ == '__main__':
  s, n = input().split(', ')
  print(front_times(s,  int(n)))
