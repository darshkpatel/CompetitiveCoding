from math import sqrt
for case in xrange(int(raw_input(''))):
    tile_x,tile_y,box_x,box_y=map(int, raw_input('').strip().split())
    if tile_y>tile_x:
        tile_x,tile_y=tile_y,tile_x
    if box_y>box_x:
        box_x,box_y=box_y,box_x

    if ((tile_x>box_x and tile_y>box_y) or (tile_y>box_x and tile_x>box_y)):
        print "Escape is possible."
    elif(tile_x > box_x and box_y >= (((2*tile_y*tile_y*box_x)+(tile_x*tile_x - tile_y*tile_y*sqrt(tile_x**2 + tile_y ** 2 - box_x ** 2)))/(tile_x**2 + tile_y**2))):
        print "Escape is possible."
    else:
        print "Box cannot be dropped."cd tmp
