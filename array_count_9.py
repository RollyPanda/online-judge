def array_count9(nums):
  return nums.count(9)

if __name__ == '__main__':
  str_nums = input().split(', ')
  nums = list(map(int, str_nums)) if str_nums[0] != '' else []
  print(array_count9(nums))
