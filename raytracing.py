def emitRay(origin,direction,figures):
    t = -1
    obj = None
    collision = False

    for figure in figures:
        r = figure.intersection(origin,direction)
        if r < 0:
            continue

        if t < 0 or r < t:
            t = r
            obj = figure
            collision = True
    
    return [t, obj, collision]