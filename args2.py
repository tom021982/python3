
def collectargs(b, e, a = 432, c = 512, *args, **kwargs):
    print(a, b, c, e)
    print(args)
    print(kwargs)

collectargs(486, 648, 437, 512, 576, 682, 768, first = 729, second = 546, third = 819)

