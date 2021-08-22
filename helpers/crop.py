from PIL import Image

dimensions = []


def crop(name, img, left, top, right, bottom):
    im = Image.open(r"" + img + "")
    im1 = im.crop((left, top, right, bottom))
    im1.save(fp=name)


# # Opens a image in RGB mode
# im = Image.open(r"betterthannothingbottom.png")
# width, height = im.size
# # Setting the points for cropped image
# """"
# grab first graph
# left = 460
# top = 310
# right = 1420
# bottom = 680
# graphheight is 320
# """
# """
# second graph
# left = 460
# top = 70
# right = 1420
# bottom = 390
# """
# left = 460
# top = 385
# right = 1420
# bottom = 710
# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))

# # Shows the image in image viewer
# im1.save(fp="newbetterthannothingbotoom.png")
