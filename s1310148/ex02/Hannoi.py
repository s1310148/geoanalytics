from abc import ABC, abstractmethod

class tHanoiAbstract(ABC):
    @abstractmethod
    def move_disk(self, source, target):
        """
        print statement to keep track of disk movement

        :param source:
        :param target:
        :return:
        """
        pass

    @abstractmethod
    def solve(self, disks, source, auxiliary, target):
        """
        solves the Tower of Hanoi using recursion

        :param disks:
        :param source:
        :param auxiliary:
        :param target:
        :return:
        """
        pass

class tHanoi(tHanoiAbstract):
    def move_disk(self, source, target):
        print('rod {} to rod {}.'.format(source, target))  
    
    def solve(self, disks, source, auxiliary, target):
        if(disks == 1):
            print('Move disk {} from'.format(disks), end=' ')
            self.move_disk(source, target)
            return
        # Creating a recursive function  
        self.solve(disks - 1, source, target, auxiliary)
        print('Move disk {} from'.format(disks), end=' ')
        self.move_disk(source, target)
        self.solve(disks - 1, auxiliary, source, target)

    def main(self):
        disks = 3
        # We are referring source as A, auxiliary as B, and target as C  
        self.solve(disks, 'A', 'B', 'C')  # Calling the function  

thanoi = tHanoi()
thanoi.main()