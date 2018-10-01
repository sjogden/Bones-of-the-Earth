endLoc = 795
platLoc = []
for x in range(0, 39):
    platLoc.append([x, 28, "bt"])
for x in range(0, 29):
    platLoc.append([-1, x, "b"])
    platLoc.append([38, x, "b"])
platLoc.append([38, 27, "d"])
platLoc.append([38, 26, "d"])
platLoc.append([38, 25, "d"])
platLoc.append([38, 24, "dt"])
for x in range(0, 5):
    platLoc.append([x, 12, "bt"])
    platLoc.append([x+5, 16, "bt"])
    platLoc.append([x+5, 8, "bt"])
    platLoc.append([x+33, 12, "bt"])
    platLoc.append([x+28, 16, "bt"])
    platLoc.append([x+28, 8, "bt"])
for x in range(13, 25):
    platLoc.append([x, 6, "bt"])
for x in range(10, 13):
    platLoc.append([x, 24, "bt"])
    platLoc.append([x+15, 24, "bt"])
for x in range(13, 17):
    platLoc.append([x, 20, "bt"])
    platLoc.append([x+8, 20, "bt"])
for x in range(21, 25):
    platLoc.append([13, x, "b"])
    platLoc.append([24, x, "b"])


skelLoc = [[6, 5],
           [6, 13],
           [29, 5],
           [29, 13]]
zombLoc = [[1, 9],
           [18, 3],
           [18, 25],
           [35, 9]]
bossLoc = [33, 25]

for platform in platLoc:
    platform[0] *= 21
    platform[1] *= 21
for skel in skelLoc:
    skel[0] *= 21
    skel[1] *= 21
for zomb in zombLoc:
    zomb[0] *= 21
    zomb[1] *= 21
bossLoc[0] *= 21
bossLoc[1] *= 21
