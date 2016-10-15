given = [1,2,3,4,4,5,6,6]
new = []
i = 0

while i < len(given):
   if (given[i] == given[i+1]):
       given.pop(given[i])
       i += 1
   else:
       i += 1
print given
