# AI course - Search platform

> Just open 'algorithms.py' file 
and implement your search algorithm then run **main.py**.

## Map data structure
Every problem has a specific map that you can run your search 
algorithm on it and check your result on report or simulated matrix.

```python
from HW1.maps import Parser
from HW1.algorithms import Search

m = Parser.get_map(0) # get a map from all maps
m.goals # coordination of all goals
m.width # width of map
m.height # height of map
m.me # start cordination
m.map_array # get map as an array
m.is_valid_cell(3,0) # if the coordination is valid to go
m.get_successors(2,1) # get list of successors
m.draw() # draw map with matplotlib

s = Search()
m.draw(algorithm=s.dfs) # pass your algorithm to see the footprint
# For algorithms with heuristics pass heuristics getter method too.
m.draw(algorithm=s.a_star,heuristics=s.get_euclidean_heuristics)
```
