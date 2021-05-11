import numpy as np

class Disk:
    def __init__(self, position:int, label:str):
        self.position = position
        self.label = label

    def update_position(self, dest:int):
        self.position = dest

class World:
    def __init__(self, size:tuple):
        self.size = size
        self.row = [0 for i in range(num_disks)]
        self.grid = [self.row for i in range(num_disks)]


    def show_disks(self, disks:list):
        for i, peg in enumerate(self.grid):
            peg[disks[i].position] = disks[i].label
            print(i, peg)

            


def hanoi_solve(disks:list, source, dest, spare):
    if len(disks) == 1:
        disks[0].update_position(dest)
    else:
        num = len(disks)-1
        hanoi_solve(disks[:num-1], disks[1].position,spare,dest)
        disks[num].update_position(dest)
        hanoi_solve(disks[:num-1], disks[1].position,dest,spare)
        world = World((num_disks, num_disks))
        world.show_disks(disks)

if __name__ == '__main__':
    num_disks = 3
    start_peg = 0
    target_peg = 2
    spare_peg = 1
    disks = []
    for i in range(num_disks):
        disks.append(Disk(start_peg, '-'*(i+1)))



    hanoi_solve(disks, start_peg, target_peg, spare_peg)
    
