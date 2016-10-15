import random
packets = []
index = 0
checking = []
for x in range (0,100):
    i = random.randint(0,1)
    packets.append(i)
print packets,

print packets[5]


for ci in range(5):
    checking.append(packets[index])
    index += 1
print checking
