"""
===================
Ordering Algorithms
===================
## Selection Sort Ordering

- find minimum or maximum
-> minimum -> select as first of the list (in sublists l[j:] for j in range(len(l)))

## Bubble Sort

- Compare consecutive elements, and switch positions if l[k]>l[k+1]

## Insertion Sort
-> separate list and insert element in front

## Merge sort
-> Divide to conquer!
-> Recursive
-> divide as you can the list into sublists, 
-> from each ordered sublist, merge with the subsequent, selecting elements in order
-> the merging part has the anallogy of 2 deck of cards -> you choose the smallest beteween the 2 top elements

## Quick Sort
-> select a pivot, and put into his right side all elements greater then him
-> all element at the left of the pivot must be smaller then him
-> based on the constrain l[i-1]<=l[i]<=l[i+1] 
"""
import pandas as pd
from IPython.display import display
import time

class Sort:
    def __init__(self, l):
        self.l = l
        self.l0 = self.l.copy()
        self.grid = 30*'-'
        self.n = len(self.l)

    def selection_sort(self, c=0, verbose=False):

        l = self.l.copy()
        n = self.n
        for j in range(n-1):
            min_index = j
            for i in range(j, n):
                if l[i]<l[min_index]:
                    min_index = i
                    c+=1
            if l[j] > l[min_index]:
                l[j], l[min_index] = l[min_index], l[j]
        if verbose:
            print('{}\n(Selection Sort)\nlist: {}\nsorted list: {}\nO({}), len(l)={}\n{}'.format(
            self.grid, self.l0, l, c, n, self.grid)
            )
        if l == sorted(self.l0): print('Selection sort , list: ', l)
        return c


    def bubble_sort(self, c=0, verbose=False):
        l = self.l.copy()
        n = self.n

        for k in range(n-1):
            for j in range(n-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    c+=1
        if verbose:
            print('{}\n(Bubble Sort)\nlist: {}\nsorted list: {}\nO({}), len(l)={}\n{}'.format(
            self.grid, self.l0, l, c, n, self.grid)
            )
        if l == sorted(self.l0): print('Bubble sort , list: ', l)
        return c

    def insertion_sort(self, c=0, verbose=False):
        l = self.l.copy()
        n = self.n

        for k in range(1, n):
            key = l[k]
            j = k -1
            while j>=0 and l[j]>key:
                l[j+1] = l[j]
                j = j-1
                c+=1
            l[j+1] = key
        if verbose:
            print('{}\n(Insertion Sort)\nlist: {}\nsorted list: {}\nO({}), len(l)={}\n{}'.format(
            self.grid, self.l0, l, c, n, self.grid)
            )
        if l == sorted(self.l0): print('Insertion sort , list: ', l)
        return c

    def merge(self, l, i, m, f, c):
        left = l[i:m]
        right = l[m:f]
        top_left, top_right = 0,0
        for k in range(i, f):
            if top_left >= len(left):
                l[k] = right[top_right]
                top_right+=1
            elif top_right >= len(right):
                l[k] = left[top_left]
                top_left+=1

            elif left[top_left] < right[top_right]:
                l[k] = left[top_left]
                top_left+=1
            else:
                l[k] = right[top_right]
                top_right+=1

            c+=1
        return c
    def merge_sort(self, 
                        l=None,  
                        i=0, 
                        f=None,
                        c=0,
                        verbose=False
                ):
        if l is None:
            l = self.l.copy()
        if f is None:
            f = len(l)

        if (f - i > 1):
            mid = (f + i)//2
            c = self.merge_sort(l, i, mid, c, verbose)
            c = self.merge_sort(l, mid, f, c, verbose)
            c = self.merge(l, i, mid, f, c)

        n = len(self.l0)
        if verbose:
            print('{}\n(Merge Sort)\nlist: {}\nsorted list: {}\nO({}), len(l)={}\n{}'.format(
            self.grid, self.l0, l, c, n, self.grid)
            )
        if l == sorted(self.l0) and len(l)==self.n: print('Merge sort , list: ', l)
        return c

    def partition(self,
                    l,
                    i,
                    f,
                    c,
                    verbose=False
                ):
        pivot = l[f] # last element as pivot
        i_ = i
        for j in range(i, f):
            if l[j] <=pivot:
                l[j], l[i_] = l[i_], l[j]
                i_+=1
            c+=1
        l[i_], l[f] = l[f], l[i_]
        if verbose:
            print(l)
        return i_, c
        
    def quick_sort(self,
                        l=None,
                        i=0,
                        f=None,
                        c=0,
                        verbose=False
                    ):
        if verbose:
            print(f"quick: {l}")
        if l is None:
            l = self.l.copy()
        if f is None:
            f = len(l)-1
        if (i < f):
            p, c = self.partition(l, i, f, c, verbose)
            c = self.quick_sort(l, i, p-1, c, verbose)
            c = self.quick_sort(l, p+1, f, c, verbose)
        
        if l == sorted(self.l0) and verbose==2:
            n = len(self.l0)
            print('{}\n(Quick Sort)\nlist: {}\nsorted list: {}\nO({}), len(l)={}\n{}'.format(
                self.grid, self.l0, l, c, n, self.grid)
                )
        if l == sorted(self.l0) and len(l)==self.n: print('Quick sort , list: ', l)
        return c


    def show_algos(self, verbose=False):
        n = self.n

        dts=[]
        t0= time.time()
        c1 = self.selection_sort(verbose=verbose)
        dts.append(time.time() - t0)

        t0= time.time()
        c2 = self.bubble_sort(verbose=verbose)
        dts.append(time.time() - t0)

        t0= time.time()
        c3 = self.insertion_sort(verbose=verbose)
        dts.append(time.time() - t0)

        t0= time.time()
        c4 = self.merge_sort(verbose=verbose)
        dts.append(time.time() - t0)
        
        t0= time.time()
        c5 = self.quick_sort(verbose=verbose)
        dts.append(time.time() - t0)

        d = {
            'Algorithm': ['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'],
            'Process time (s)': dts,
            'O(n)': [f'O({c1})', f'O({c2})', f'O({c3})', f'O({c4})', f'O({c5})',]
        }
        df = pd.DataFrame(d)
        df.index._name = f'len(l)={n}'
        df = df.sort_values(['Process time (s)'], ascending=True)
        df = df.reset_index(drop=True)
        display(df)

def main(verbose=False):
    l = [7,5,1,8,3]
    
    if verbose:
        print('algorithms: {}'.format(
            list(filter(lambda x: '__' not in x, dir(Sort(l))))
        ))
    
    Sort(l).show_algos()


def sort_list(l, algorithm, verbose=False):
    assert type(l) == list, "l must be a list."
    assert type(algorithm) == str, "algorithm must be a string in ['selection','bubble','insertion','merge','quick','all']"
    
    if algorithm=='selection':
        Sort(l).selection_sort(verbose=verbose)
    elif algorithm=='bubble':
        Sort(l).bubble_sort(verbose=verbose)
    elif algorithm=='insertion':
        Sort(l).insertion_sort(verbose=verbose)
    elif algorithm=='merge':
        Sort(l).merge_sort(verbose=verbose)
    elif algorithm=='quick':
        Sort(l).quick_sort(verbose=verbose)
    elif algorithm == 'all':
        Sort(l).show_algos()
    else:
        print("No algorithm selected. algorithm must be a string in ['selection','bubble','insertion','merge','quick','all'].")

if __name__ == "__main__":
    main()
