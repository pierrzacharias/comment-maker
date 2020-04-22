# Simple python script to generate comment for any language
Use : python generate.py <language_comment_sign> <comment_to_add>
You can use it directly in vim e.g for python:
```
:r! python ~/Documents/comment_generator/generator.py '\#' "t"
```
(Special characters like '#' or '%' in vim need a '\' above.)
![](screenshot.png) 
