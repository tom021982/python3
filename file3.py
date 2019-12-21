
f1 = open(r'/root/pythonTraining/dishes')
stuff = f1.readlines()
f1.close()
stuff[2] = "Ruby is an excellent oops dev language \n"
f1 = open(r'/root/pythonTraining/dishes','w')
f1.writelines(stuff)
f1.close()

