sum = 0
sum_squares = 0
for n in range(1, 101):
    sum += n
    sum_squares += n * n
print ((sum * sum) - sum_squares)
