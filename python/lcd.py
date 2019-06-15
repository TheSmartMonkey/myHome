# coding: UTF-8
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Create display object - Créé un objet display
class LCD(object):
    def __init__(self):
        # Create display object - Créé un objet display
        self.lcd = Adafruit_SSD1306.SSD1306_128_32(rst = None)

        # init display - Initialise l'écran
        self.lcd.begin()

        # Clear display - Efface l'écran
        self.lcd.clear()
        self.lcd.display()

    def displayText(self,line1,line2):
        """
        Create blank image for drawing with mode '1' for 1-bit color
        Créé un image avec un codage des couleurs sur 1 bit (noir et blanc)
        """

        width = self.lcd.width # Screen width - Largeur de l'écran
        height = self.lcd.height # Screen height - Hauteur de l'écran

        # Get drawing object to draw on image - On créé un objet sur lequel on va dessiner
        self.image = Image.new('1', (width, height))

        self.draw = ImageDraw.Draw(self.image) # Handles the image - Manipule l'image
        self.font = ImageFont.truetype(font = "batmfa__.ttf", size = 15) # Text font - Police de caractère
        self.draw.text((0,0), line1, font = self.font, fill = 255) # Line 1 - Ligne 1
        self.draw.text((0,16), line2, font = self.font, fill = 255) # Line 2 - Ligne 2
        
        #  Update display - Actualise l'affichage
        self.lcd.image(self.image)
        self.lcd.display()

if __name__=="__main__":                                                                                             
    from time import sleep
    lcd = LCD()
    for message1,message2 in (("Ouverture","Porte"),("Porte","Ouverte"),("Fermeture","Porte"),("Porte","Fermée")):
        lcd.displayText(message1, message2)
        sleep(1)