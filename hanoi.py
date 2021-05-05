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
            # print(i, peg)

            


def hanoi_solve(disks, source, dest, spare):
    print(disks)
    num = len(disks)
    if num == 1:
        disks[0].update_position(dest)
    else:
        hanoi_solve(num-1, disks[1].position,spare,dest)




    


if __name__ == '__main__':
    num_disks = 3
    start_peg = 0
    target_peg = 2
    spare_peg = 1
    disks = []
    for i in range(num_disks):
        disks.append(Disk(start_peg, '-'*(i+1)))

    world = World((num_disks, num_disks))
    world.show_disks(disks)

    hanoi_solve(disks, start_peg, target_peg, spare_peg)
    
