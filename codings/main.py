# import numpy as np

# img1 = np.zeros((256,256))
# img30 = np.zeros((256,256))
# img15 = interpolate(img1,img30)
# img7 = interpolate(img1,img15)
# img4 = interpolate(img1,img7)
# img2 = interpolate(img1,img4)
# img3 = interpolate(img2,img4)
# img5 = interpolate(img4,img7)
# img6 = interpolate(img5,img7)
# img11 = interpolate(img7,img15)
# img13 = interpolate(img11,img15)
# img14 = interpolate(img13,img15)
# img12 = interpolate(img11,img13)
# img9 = interpolate(img7,img11)
# img8 = interpolate(img7,img9)
# img10 = interpolate(img9,img11)
# img23 = interpolate(img15,img30)
# img19 = interpolate(img15,img23)
# img17 = interpolate(img15,img19)
# img16 = interpolate(img15,img17)
# img18 = interpolate(img17,img19)
# img21 = interpolate(img19,img23)
# img20 = interpolate(img19,img21)
# img22 = interpolate(img21,img23)
# img26 = interpolate(img23,img30)
# img28 = interpolate(img26,img30)
# img27 = interpolate(img26,img28)
# img29 = interpolate(img28,img30)
# img24 = interpolate(img23,img26)
# img25 = interpolate(img24,img26)


import math
def getTileBounds(tileX, tileY, zoom):
    tileSize = 256
    mapSize = tileSize * math.pow(2, zoom)
    originShift = 20037508.34   
    minX = (tileX * tileSize / mapSize) * (2 * originShift) - originShift
    maxY = originShift - (tileY * tileSize / mapSize) * (2 * originShift)
    maxX = ((tileX + 1) * tileSize / mapSize) * (2 * originShift) - originShift
    minY = originShift - ((tileY + 1) * tileSize / mapSize) * (2 * originShift)
    
    return [minX, minY, maxX, maxY]


result = getTileBounds(11,7,4)
result = map(str,result)
print('%2C'.join(result))