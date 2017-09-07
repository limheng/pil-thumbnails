from PIL import Image
import os

# Will search all .jpg files in variable picturefolder
# Will create a folder in variable thumbfolder
# Will resize images to specified ratio/size
# Will crop the top-center of the image

def create_thumbnail(picture, savefile, multip = 150, rwidth = 5, rheight = 7):
    savesize = (rwidth * multip, rheight * multip)
    image = Image.open(picture)
    ratio = rwidth / rheight

    hsize = image.size[1]
    if image.size[0] < savesize[0]:
        wpercent = (savesize[0]/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((savesize[0],hsize), Image.ANTIALIAS)

    if hsize < savesize[1]:
        hpercent = (savesize[1]/float(image.size[1]))
        wsize = int((float(image.size[0])*float(hpercent)))
        image = image.resize((wsize,savesize[1]), Image.ANTIALIAS)

    owidth, oheight = image.size
    width = min(owidth, oheight * ratio)
    height = min(owidth/ratio, oheight)
    x = (owidth - width) // 2
    y = 0
    box = (x, y, x + width, y + height)
    standard = image.crop(box)
    standard.thumbnail(savesize, Image.ANTIALIAS)
    standard.save(savefile, "JPEG")
    return savefile

pictures = []
picturefolder = 'pictures'
thumbfolder = 'thumbnails'
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), picturefolder)
for root, dirs, files in os.walk(path):
    if root.find('\\' + thumbfolder) < 0:
        for file in files:
             if file.endswith(".jpg") or file.endswith(".JPG"):
                picture = os.path.join(root, file)
                pictures.append(picture)

directory = os.path.join(path, thumbfolder)
if not os.path.exists(directory):
    os.makedirs(directory)

for i, pic in enumerate(pictures):
    standard = os.path.join(directory, os.path.basename(pic))
    standpic = create_thumbnail(pic, standard, 3, 71, 96)
