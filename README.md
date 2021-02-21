=================================

# Ordering Algorithms
=================================


Implementation of a class (Order) with methods of the sorting algorithms:
- Selection Sort
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

## Usage

            >>> from Ordering_Algorithms import sort_list
            >>> l = [234, 123, 657, 23 ,789, 234]

- Display of all algorithms and processing time: 

            >>> sort_list(l, 'all')
            Selection sort , list:  [23, 123, 234, 234, 657, 789]
            Bubble sort , list:  [23, 123, 234, 234, 657, 789]
            Insertion sort , list:  [23, 123, 234, 234, 657, 789]
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 234, 789]
            [123, 234, 657, 23, 234, 789]
            Merge sort , list:  [23, 123, 234, 234, 657, 789]
            [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
                    Algorithm  Process time (s)   O(n)
            0  Insertion Sort          0.000023   O(6)
            1     Bubble Sort          0.000031   O(6)
            2      Quick Sort          0.000075   O(9)
            3  Selection Sort          0.000082   O(5)
            4      Merge Sort          0.000150  O(16)

- insertion sort

            >>> sort_list(l, 'insertion')
            Insertion sort , list:  [23, 123, 234, 234, 657, 789]

- bubble sort

            >>> sort_list(l, 'bubble')
            Bubble sort , list:  [23, 123, 234, 234, 657, 789]

- quick sort

            >>> sort_list(l, 'quick')
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]
            Quick sort , list:  [23, 123, 234, 234, 657, 789]

- selection sort

            >>> sort_list(l, 'selection')
            Selection sort , list:  [23, 123, 234, 234, 657, 789]

- merge sort

            >>> sort_list(l, 'merge')
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [234, 123, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 789, 234]
            [123, 234, 657, 23, 234, 789]
            [123, 234, 657, 23, 234, 789]
            Merge sort , list:  [23, 123, 234, 234, 657, 789]
            [23, 123, 234, 234, 657, 789]

- OBS: Note that the recursive algorithms (merge and quick) have high verbose, because printing is included in the recursive function

## Algorithms 
### Selection Sort Ordering

- find minimum or maximum
- minimum -> select as first of the list (in sublists l[j:] for j in range(len(l)))

### Bubble Sort

- Compare consecutive elements, and switch positions if l[k]>l[k+1]

### Insertion Sort
- separate list and insert element in front

### Merge sort
- Divide to conquer!
- Recursive
- divide as you can the list into sublists, 
- from each ordered sublist, merge with the subsequent, selecting elements in order
- the merging part has the anallogy of 2 deck of cards -> you choose the smallest beteween the 2 top elements

### Quick Sort
- select a pivot, and put into his right side all elements greater then him
- all element at the left of the pivot must be smaller then him
- based on the constrain l[i-1]<=l[i]<=l[i+1] 


## Author:
- Pedro Blöss Braga

## Useful Links:
- (Portuguese) Algoritmos de ORDENAÇÃO https://www.youtube.com/playlist?list=PL5TJqBvpXQv4l7nH-08fMfyl7aDFNW_fC
