endLoc = 1612
platLoc = []
for x in range(0, 77):
    platLoc.append([x, 28, "bt"])
for x in range(0, 29):
    platLoc.append([-1, x, "b"])
    platLoc.append([77, x, "b"])
platLoc.append([77, 27, "d"])
platLoc.append([77, 26, "d"])
platLoc.append([77, 25, "d"])
platLoc.append([77, 24, "dt"])
for x in range(0, 6):
    for y in range(0, 5):
        platLoc.append([15-x, 4+y+4*x, "b"])
##    platLoc.append([x-4, 11, "b"])
##    platLoc.append([x-4, 12, "b"])
##    platLoc.append([x-4, 13, "b"])
##    platLoc.append([x-4, 14, "b"])
platLoc.append([19, 0, "bt"])
platLoc.append([19, -1, "b"])
platLoc.append([23, 0, "bt"])
platLoc.append([23, -1, "b"])
platLoc.append([19, 3, "bt"])
platLoc.append([23, 3, "bt"])
platLoc.append([23, 4, "b"])
for x in range(4, 25):
    platLoc.append([19, x, "b"])
for x in range(20, 23):
    platLoc.append([x, 4, "b"])
for x in range(20, 32):
    platLoc.append([x, 12, "bt"])
for x in range(27, 50):
    platLoc.append([x, 24, "bt"])
for x in range(33, 47):
    platLoc.append([x, 20, "bt"])
    platLoc.append([x, 12, "bt"])
    platLoc.append([x+3, 16, "bt"])
for x in range(4, 21):
    platLoc.append([32, x, "b"])
for x in range(5, 28):
    platLoc.append([50, x, "b"])
platLoc.append([36, 8, "bt"])
platLoc.append([37, 8, "bt"])
platLoc.append([38, 8, "b"])
platLoc.append([38, 7, "bt"])
platLoc.append([39, 7, "b"])
platLoc.append([39, 6, "bt"])
platLoc.append([40, 6, "b"])
platLoc.append([40, 5, "bt"])
platLoc.append([41, 5, "b"])
for x in range(41, 57):
    platLoc.append([x, 4, "bt"])

skelLoc = [[20, 1],
           [47, 13],
           [47, 21],
           [47, 25]]
zombLoc = [[13, 25],
           [25, 9],
           [33, 17],
           [53, 25],
           [70, 25]]

for platform in platLoc:
    platform[0] *= 21
    platform[1] *= 21
for skel in skelLoc:
    skel[0] *= 21
    skel[1] *= 21
for zomb in zombLoc:
    zomb[0] *= 21
    zomb[1] *= 21
