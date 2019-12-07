for x in xrange(int(raw_input(''))):
    vars = [int(n) for n in raw_input('').split()]
    sides = map(int, raw_input('').split())
    n_sides=vars[0]
    a=vars[1]
    b=vars[2]
    pof_a=sides.count(a)/float(n_sides)
    pof_b=sides.count(b)/float(n_sides)
    print pof_a*pof_b