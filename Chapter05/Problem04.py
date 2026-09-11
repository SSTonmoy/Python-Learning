# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
# length of s after these operations? => maube 3. but no it will be 2.
s.add('20')
print(s)
