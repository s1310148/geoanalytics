# Python program to implement Pigeonhole Sort */
 
# source code : "https://en.wikibooks.org/wiki/
#   Algorithm_Implementation/Sorting/Pigeonhole_sort"
from abc import ABC, abstractmethod

class pigeonHoleSortAbstract(ABC):
    @abstractmethod
    def sort(self, arr):
        """
        Implements pigeonHole sorting algorithm

        :param arr:
        :return:
        """
        pass
class pigeonHole(pigeonHoleSortAbstract):
    def sort(self, a):
        my_min = min(a)
        my_max = max(a)
        size = my_max - my_min + 1
    
        # our list of pigeonholes
        holes = [0] * size
    
        # Populate the pigeonholes.
        for x in a:
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
    
        # Put the elements back into the array in order.
        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                a[i] = count + my_min
                i += 1        

    def main(self):
        import random
        a = []
        for _ in range(100):
            a.append(random.randint(1, 100))

        print("Sorted order is : ", end = ' ')
        self.sort(a)
        for i in range(0, len(a)):
            print(a[i], end = ' ')

pigeonHole = pigeonHole()
pigeonHole.main()