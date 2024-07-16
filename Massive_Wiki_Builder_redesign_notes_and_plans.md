# Massive Wiki Builder redesign notes and plans

2022-09-18: Bill has drawn a dataflow style diagram with two aims in mind:  
1. illustrate the top-level Massive Wiki builder data processing; and  
2. calling out key datastructures that can be refactored into a multi-purpose data structure to support MW website properties:  
	- fuzzy linking of wiki pages  
	- wiki full-text search  
	- multiple views of all wiki pages: by name, by date, and link to most-recent changed subset.  

![[MWB-dataflowV3.png]]
