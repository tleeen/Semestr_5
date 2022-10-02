import numpy as np

arr = np.char.array(["Python", "PHP", "JS", "examples", "html"])
c = np.char.count(arr, "P")
print("Колличество P: ")
print(c)