def hanoi_display(towers):
    h = towers[0]
    rows = [""] * h
    for i in range(h):
        for tower in towers[1:]:
            if len(tower) >= (h-i):
                rows[i] += "-" * tower[h-i-1]
                rows[i] += " " * (h - tower[h-i-1] + 2)
            else:
                rows[i] += "|"
                rows[i] += " " * (h + 1)
    print "\n".join(rows)

def hanoi_rec(h, draw=True):
    steps = []
    towers = [h, list(reversed(range(1, h+1))), [], []]
    
    hanoi_rec_move(steps, towers, h, 1, 3, 2, draw)

    if draw:
        hanoi_display(towers)
    
    return steps

def hanoi_rec_move(steps, towers, n_disks, tower_from, tower_to, tower_bridge, draw):
    if n_disks <= 0:
        return

    hanoi_rec_move(steps, towers, n_disks - 1, tower_from, tower_bridge, tower_to, draw)
    steps.append(towers[1:])
    
    if draw:
        hanoi_display(towers)
        print "Moving disk from tower %d to tower %d..." % (tower_from, tower_to)

    disk = towers[tower_from].pop()
    towers[tower_to].append(disk)
    hanoi_rec_move(steps, towers, n_disks - 1, tower_bridge, tower_to, tower_from, draw)
