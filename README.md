# poynter - *worse of both worlds*

### Features
Have you ever wanted to have the same fun with Python as you have with C?

Do you long for a segmentation fault without having to use SWIG or similar?

Do you miss the random segmentation faults when accessing memory out of bounds?

Do you want to shoot your self in the foot with a Python?

Do you want to be equals to your embedded developer colleagues?

Do you want to write to memory you shouldn't write to without these pesky IndexOutOfRangeException?

&rarr; No?


&rarr; Great! This is why we didn't spare any expenses and developed a real python poynter.
Now with true random segmentation faults when reading memory out of bounds, a real size_t type and much, much more!

 --- 
### Customer comments
But don't just trust us. See what our customers have to say about our product:

&rarr; "This is worse than hell!" - *ARM Limited*

&rarr; "Why should I ever use this?" - *Guido van Rossum*

&rarr; "Is this a joke? Am I a joke to you?" - *Elon Musk*

&rarr; "Ahh kill me now, I cannot un-see this ... ever! There is no God" - *God*

&rarr; "The user you have called is currently not available!" - *Google*

&rarr; "Nice! It is perfect." - *Rice Powell*

&rarr; "What have I done? All is lost!" - *Library author*

### Examples:

```python
from poynter import malloc, free

data_ptr = malloc(10)
data_ptr[3] = 15
print(data_ptr[100]) # Might result in a segmentation fault, but if you are lucky, it doesn't
free(data_ptr) # Don't forget this, we need to free our memory, otherwise:segmentation fault
```
