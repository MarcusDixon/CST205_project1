#Marcus Dixon
#CST 205
#Project 1
#Description: CST205 Project 1 Image manipulation to replace undesireable pixels in a set of otherwise similar images.

folder = "file path"

#create an array list of pictures
pictures = []

#append the chosen image to the pictures list
for i in range(0, 9):
	imageFile = pickAFile()
	imageDisplay = makePicture(imageFile)
	pictures.append(imageDisplay)

#create an empty picture for the final image
finalImage = makeEmptyPicture(495, 557)

#function to obtain median values
def medianOdd(values):
  listLength = len(values)
  sortedValues = sorted(values)
  middleIndex = (listLength/2)
  return sortedValues[middleIndex]

#create lists for red, green, and blue values
redValue = []
greenValue = []
blueValue = []

for w in range(0, 495):
  for y in range(0, 557):
    for p in range(0, 9):
      #get pixel at pictures[p] pixel, with w as x-coordinate and y as y-coordinate
      imagepixel = getPixel(pictures[p], w, y)
		
      #append red, blue, and green pixel to respective value list
      redValue.append(getRed(imagepixel))
      blueValue.append(getBlue(imagepixel))
      greenValue.append(getGreen(imagepixel))
		
    #set redness, blueness, and greeness of pixel at (finalImage, w, y) with value medianOdd()
    setRed(getPixel(finalImage, w, y), medianOdd(redValue))
    setBlue(getPixel(finalImage, w, y), medianOdd(blueValue))
    setGreen(getPixel(finalImage, w, y), medianOdd(greenValue))
    redValue = []
    blueValue = []
    greenValue = []

#display final image
show(finalImage)