
# Algorytmy Planowania Procesów

Implementacja różnych algorytmów planowania procesów w języku Python, symulacja działania algorytmów zastępowania stron oraz algorytmów planowania czasu procesora.

## Opis

Ten projekt zawiera symulacje działania algorytmów zastępowania stron:
- FIFO (First-In, First-Out)
- LFU (Least Frequently Used)
 
oraz algorytmów planowania czasu procesora:
- FCFS (First-Come, First-Served)
- LCFS (Last-Come, First-Served)

## Sposób działania:

### FCFS (First-Come, First-Served):

Algorytm ten działa na zasadzie obsługi procesów w kolejności, w jakiej się pojawiły w systemie.
Procesy są kolejkowane według czasu ich przyjścia (arrival time) i wykonywane w tej kolejności.
Gdy proces zostanie wykonany, algorytm przechodzi do obsługi kolejnego procesu w kolejce.

### LCFS (Last-Come, First-Served):

Algorytm ten działa na zasadzie obsługi procesów w kolejności od ostatniego dodanego do pierwszego obsługiwanego.
Procesy są kolejkowane według czasu ich przyjścia (arrival time) i wykonywane w kolejności od ostatnio dodanego procesu do pierwszego.
Gdy proces zostanie wykonany, algorytm przechodzi do obsługi kolejnego procesu w kolejce.

### FIFO (First-In, First-Out):

Algorytm FIFO jest stosowany w zastępowaniu stron w pamięci podręcznej (cache).
Polega na usuwaniu z pamięci podręcznej najstarszych stron, które zostały dodane jako pierwsze (First-In).
Nowe strony są dodawane na koniec kolejki, a najstarsze usuwane są jako pierwsze.

### LFU (Least Frequently Used):

Algorytm LFU również stosowany jest w zastępowaniu stron w pamięci podręcznej (cache).
Polega na usuwaniu z pamięci podręcznej stron, które były używane najrzadziej (Least Frequently Used).
Strona, która była używana najrzadziej, jest zastępowana nową stroną, gdy pamięć podręczna jest pełna.

### Użycie:
Należy dołączyć wszystkie pliki i uruchomić program.
W pliku 'main.py' dla 'getProcesses()' oraz 'List_of_numbers()' można dostosować zakres losowanych parametrów/liczb poprzez zmienienie wartości przekazywanych do tych funkcji.

*** 

# Process Scheduling Algorithms

Implementation of various process scheduling algorithms in Python, simulation of page replacement algorithms, and CPU scheduling algorithms.

## Description

This project includes simulations of the following page replacement algorithms:
- FIFO (First-In, First-Out)
- LFU (Least Frequently Used)

as well as CPU scheduling algorithms:
- FCFS (First-Come, First-Served)
- LCFS (Last-Come, First-Served)

## Functioning:

### FCFS (First-Come, First-Served):

This algorithm operates by servicing processes in the order they appeared in the system.
Processes are queued based on their arrival time and executed in that order.
Once a process is executed, the algorithm moves on to service the next process in the queue.

### LCFS (Last-Come, First-Served):

This algorithm operates by servicing processes in the order from the most recently added to the first serviced.
Processes are queued based on their arrival time and executed in the order from the most recently added process to the first.
Once a process is executed, the algorithm moves on to service the next process in the queue.

### FIFO (First-In, First-Out):

The FIFO algorithm is used in page replacement in cache memory.
It involves removing the oldest pages from the cache memory, which were added first (First-In).
New pages are added to the end of the queue, and the oldest ones are removed first.

### LFU (Least Frequently Used):

The LFU algorithm is also used in page replacement in cache memory.
It involves removing the pages from the cache memory that were least frequently used.
The page that was least frequently used is replaced with a new page when the cache memory is full.

### Usage:
All files should be included and the program run.
In the 'main.py' file, for 'getProcesses()' and 'List_of_numbers()', the range of randomly generated parameters/numbers can be adjusted by changing the values passed to these functions.


 
