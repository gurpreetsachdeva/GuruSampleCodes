# Used when you want to transform one list into another without writing iterating code
time_in_minutes=[3,5,9]
time_in_seconds=[60*i for i in time_in_minutes]
print(time_in_seconds)
