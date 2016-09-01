from PIL import Image
import statistics
pic1 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/1.png')
pic2 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/2.png')
pic3 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/3.png')
pic4 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/4.png')
pic5 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/5.png')
pic6 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/6.png')
pic7 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/7.png')
pic8 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/8.png')
pic9 = Image.open('/Users/markkinoshita/Desktop/CST205Project1/Project1Images/9.png')

ImageList = [pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9]

NewImage = Image.new("RGB", (495,557))



