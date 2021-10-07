# Libraries
import pandas

# some random cool thing
from tqdm import tqdm
loop = tqdm(total = 5000, position=0, leave=False)
for k in range(5000):
    loop.set_description("Loading code...".format(k))
    loop.update(1)
loop.close()
start = 0
end = 12
from tqdm import tqdm
loop = tqdm(total = 2000, position=0, leave=False)
for k in range(2000):
    loop.set_description("Grabbing user info...".format(k))
    loop.update(1)
loop.close()
print("Code loaded... 100%|███████████████████████████████████████████████████████ | 5000/5000 ")
print("User info grabbed... 100%|███████████████████████████████████████████████████████ | 2000/2000 ")


#introduction
print("""
 _______ _                     _______      _     _       
(_______|_)                   (_______)    | |   | |      
 _       _ ____   ____  ___    _       ____| | _ | | ____ 
| |     | |    \ / _  )/___)  | |     / _  | || \| |/ _  )
| |_____| | | | ( (/ /|___ |  | |____( ( | | |_) ) ( (/ / 
 \______)_|_|_|_|\____|___/    \______)_||_|____/|_|\____)
                                                          
""")
name =input("Hello, in order to get started, I would like to know your name:\n=" )
print("Nice to meet you", name)
print("In order for me to start making your time table I need to know which number you would like me to mutiply, please type it beneath")
multiple = input("Mutiple\n=")

count = start
while count <= end:
    product = count * multiple
    print(count, "x", multiple, "=", product)
    count += 1


# Variables
start = 0
end = 12

# Ideas Done
# Loading Bar Done
#Asking for numbre Done
# Table   In progress
