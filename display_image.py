from PIL import Image

with Image.open("test_images/pattern.jpg") as image:
    image.show()
