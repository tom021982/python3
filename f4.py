# To pass keyword variable length arguments

def bikes_make(**kwargs):
    if kwargs is not None:
        print(kwargs)

bikes_make(GTX='Suzuki', FTZ='Yamaha')
