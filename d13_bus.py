f = open("./d13_input.txt","r").read()
f = f.split("\n")
target = int(f[0].rstrip())
buses = [x for x in f[1].rstrip().split(",")]
# best = None
# closest = float("inf")
# for bus in buses:
#     if target % bus == 0:
#         best = bus
#         break
#     else:
#         cur = bus - (target % bus)
#         if cur < closest:
#             best = bus
#             closest = cur
for i in range(len(buses)):
    if buses[i] != "x":
        buses[i] = int(buses[i])

distances = []
for i in range(len(buses)):
    if buses[i] != "x":
        distances.append(i-0)
    else:
        distances.append("*")
buses = [(x,y) for x,y in zip(buses,distances) if x != "x"]

def findDeparture(t, bus):
    rem = t%bus
    return t if rem == 0 else t + (bus - rem)
def nextDeparture(bus, dist, firstBus, m):
    while (bus*m)%firstBus != dist:
        m+=1
    return m

t = findDeparture(max([x for x,y in buses]), buses[0][0])

def checkBus(buses, t, i, level = 1):
    if i >= len(buses):
        return True
    bus, dist = buses[i]
    if (t+dist)%bus == 0:
        return checkBus(buses, t, i+1, level + 1)
    return False

def part2(buses,t,i):
    bus, dist = buses[i]
    m = t // bus + 1 if t % bus else t // bus
    m = nextDeparture(bus, dist, buses[0][0], m)

    while not checkBus(buses,(m*bus)-dist, i+1):
        m = nextDeparture(bus,dist,buses[0][0], m+1)
    return [m,bus]

print(part2(buses,415579909629976,1))
# print(buses)
# print(findDeparture(291698225,29))
# t, step = 0, 1
# p2 = buses
# iterate through buses
# for bus_id, mins in p2:
#     # check to see if bus is departing at current time
#     while (t + mins) % bus_id != 0:
#         t += step
#     # increase step multiple to find next min for next bus
#     step *= bus_id

# print(f'Part 2: {t}')c