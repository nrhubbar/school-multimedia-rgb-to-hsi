#Nicholas Hubbard
from PIL import Image
import numpy


def gethue(r,g,b):
    sumRGB = sum((r, g, b))
    r /= sumRGB
    g /= sumRGB
    b /= sumRGB
    numerator = .5 * ((r-g) + (r-b))
    denomanator = ((((r-g)**2) + ((r-b)*(g-b)))**.5)
    theta = numpy.arccos(numerator/(denomanator + .000001))
    return float(theta) if b <= g else float(360 - theta)


def getintensity(r,g,b):
    return (r+g+b) / 3


def getsaturation(r,g,b):
    return 1 - (3 * min(r,g,b))

hsi = {"hue" : gethue, "intensity" : getintensity, "saturation" : getsaturation}
picture = Image.open("fieldscape-picture-rgb.jpg")
print("opened image")
pictureArray = numpy.asarray(picture)
for key in hsi.keys():
    keyList = []
    for i in range(picture.height):
        keyList.append([])
        for j in range(picture.width):
            keyList[i].append(numpy.uint8(hsi[key](*pictureArray[i][j])))

    keyArray = numpy.asarray(keyList)
    keyImage = Image.fromarray(keyArray)
    keyImage.save("{}.bmp".format(key))


print("Done")
