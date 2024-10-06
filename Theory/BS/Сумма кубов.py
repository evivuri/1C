def check_sum_of_cubes(x):
  """Проверяет, можно ли представить число x как сумму кубов двух целых положительных чисел."""
  for a in range(1, int(x *(1/3)) + 1):
    b_cube = x - a *3
    if b_cube > 0 and int(b_cube *(1/3)) *3 == b_cube:
      return True
  return False

# Ввод количества тестовых случаев
t = int(input())

# Обработка каждого тестового случая
for _ in range(t):
  x = int(input())
  if check_sum_of_cubes(x):
    print("YES")
  else:
    print("NO")