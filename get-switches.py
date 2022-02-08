# open file to read
f = open('switches.txt')
try:
    # read lines and splint of '/n'
    f_list = f.read().splitlines()
# close file
finally:
    f.close()

for each in f_list:
    print(each.split(":")[0])