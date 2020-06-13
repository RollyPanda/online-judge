def string_times(s, n):
  return s * n
  
if __name__ == '__main__':
  s, n = input().split(', ')
  print(string_times(s,  int(n)))
