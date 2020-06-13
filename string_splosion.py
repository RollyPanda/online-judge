def string_splosion(s):
  a = ""
  for i in range(len(s)):
    a += s[:i + 1]
  return a

if __name__ == '__main__':
  s = input()
  print(string_splosion(s))
