from PIL import Image
import os

def create_thumbnail(picture, savefile, multip=150, rwidth=5, rheight=7):
    """ Resize images to specified ratio/size.
        Crops the top-center of the image.
    """
    savesize = (rwidth * multip, rheight * multip)
    image = Image.open(picture)
    ratio = rwidth / rheight

    hsize = image.size[1]
    if image.size[0] < savesize[0]:
        wpercent = (savesize[0] / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((savesize[0], hsize), Image.ANTIALIAS)

    if hsize < savesize[1]:
        hpercent = (savesize[1] / float(image.size[1]))
        wsize = int((float(image.size[0]) * float(hpercent)))
        image = image.resize((wsize, savesize[1]), Image.ANTIALIAS)

    owidth, oheight = image.size
    width = min(owidth, oheight * ratio)
    height = min(owidth / ratio, oheight)
    x = (owidth - width) // 2
    y = 0
    box = (x, y, x + width, y + height)
    standard = image.crop(box)
    standard.thumbnail(savesize, Image.ANTIALIAS)
    standard.save(savefile, "JPEG")
    return savefile

def main():
    """ Searches folder for each .jpg file
        then generates a thumnail for each file found.
    """
    pictures = []
    picturefolder = 'pictures'
    thumbfolder = 'thumbnails'
    filepath = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(filepath, picturefolder)
    for root, dirs, files in os.walk(path):
        if root.find('\\' + thumbfolder) < 0:
            for f in files:
                if f.endswith(".jpg") or f.endswith(".JPG"):
                    picture = os.path.join(root, f)
                    pictures.append(picture)

    directory = os.path.join(path, thumbfolder)
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, pic in enumerate(pictures):
        standard = os.path.join(directory, os.path.basename(pic))
        standpic = create_thumbnail(pic, standard, 3, 71, 96)

if __name__ == '__main__':
    main()
