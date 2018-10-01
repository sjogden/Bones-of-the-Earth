endLoc = 2515
platLoc = []
for x in range(0, 121):
    platLoc.append([x, 28, "bt"])
platLoc.append([120, 27, "d"])
platLoc.append([120, 26, "d"])
platLoc.append([120, 25, "d"])
platLoc.append([120, 24, "dt"])
platLoc.append([25, 27, "b"])
platLoc.append([25, 26, "b"])
platLoc.append([25, 25, "b"])
platLoc.append([25, 24, "bt"])
platLoc.append([46, 27, "bt"])
platLoc.append([60, 27, "bt"])
platLoc.append([72, 27, "bt"])
platLoc.append([76, 27, "bt"])

skelLoc = [[57, 25]]
zombLoc = [[73, 25]]

for platform in platLoc:
    platform[0] *= 21
    platform[1] *= 21
for skel in skelLoc:
    skel[0] *= 21
    skel[1] *= 21
for zomb in zombLoc:
    zomb[0] *= 21
    zomb[1] *= 21
