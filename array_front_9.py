def array_front9(nums):
  return 9 in nums[:4]

if __name__ == '__main__':
  str_nums = input().split(', ')
  nums = list(map(int, str_nums)) if str_nums[0] != '' else []
  print(array_front9(nums))

  
