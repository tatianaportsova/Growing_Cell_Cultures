# Growing_Cell_Cultures - A Variation of Game of Life
### Coding Challenge - Growing cell cultures in a medium 

Initially presented with an empty grid that consists of unlivable (marked as ".") and livable (marked as "L") zones.
After populating the grid with cultures, we can start counting hours/iterations of how long it'll take for the cultures to stabilize:
```sh

 ∙ If a livable area is empty and there are no adjacent cell cultures, the cells will take hold and begin to grow.
 
 ∙ If a culture is growing in a location where four or more adjacent locations are also occupied, then the culture dies back.
 
 ∙ Unlivable spaces are never occupied with a culture. 

 ∙ Otherwise, no change occurs.
```

Run an example:
```sh
python code.py
```
Running that command displays the following output in a terminal:
```sh
•	Number of hours (iterations) it takes to stabilize the cultures

•	Number of unlivable cell locations in the grid

•	Number of cell locations that are occupied with cultures on the final day (when it stabilizes)
 
•	The ratio of spaces upon which the culture has taken hold to total Livable spaces on the final day as a percentage
```
