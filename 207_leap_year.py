def check_leap_year(start_year, end_year):
    answer = [ i for i in range(start_year, end_year+1)
        if i % 4 == 0 and i % 400 != 0]
    return answer
print(check_leap_year(1950, 2050));