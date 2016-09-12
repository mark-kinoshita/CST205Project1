from PIL import Image
# import the Python Image Library
pic1 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/1.png')
pic2 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/2.png')
pic3 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/3.png')
pic4 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/4.png')
pic5 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/5.png')
pic6 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/6.png')
pic7 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/7.png')
pic8 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/8.png')
pic9 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/9.png')

# Open all the images

pic1.load()
pic2.load()
pic3.load()
pic4.load()
pic5.load()
pic6.load()
pic7.load()
pic8.load()
pic9.load()
# Load all the images so we can access the data


theImages = [pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9]
# Add this images to a list
width, height = pic1.size
# Get the size of the images and store data in variables

redPixelList = []
greenPixelList = []
bluePixelList = []
# Create three lists to store the RBG data from the pixels of the images

for x in range(0, width):
    for y in range(0, height):
        for myImage in theImages:

            myRed, myGreen, myBlue = myImage.getpixel((x, y))

            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
# Iterate through the images and save the pixel data into lists


def medianodd(num):

    listLength = len(num)
    sortedValues = sorted(num)
    middleIndex = ((listLength + 1)/2) - 1
    return sortedValues[middleIndex]
# Function to determine the median value for the lists obtained above

medianodd(redPixelList)

medianodd(greenPixelList)

medianodd(bluePixelList)

# Function calls for each list

mynewImage = Image.new("RGB", (width, height))

# Create new empty image with correct width and height

mynewImage.load()

# Load new image

for x in range(0, width):
    for y in range(0, height):
        mynewImage.putpixel((x, y), (medianodd(redPixelList), medianodd(greenPixelList), medianodd(bluePixelList)))

# Give new image median pixel values

mynewImage.show()

# Outputs new image

# Github link:https://github.com/mkinoshita22/CST205Project1










