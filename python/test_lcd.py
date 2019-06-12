# coding: UTF-8                                                          
import Adafruit_GPIO.SPI as SPI                                          
import Adafruit_SSD1306                                                  

from PIL import Image                                                    
from PIL import ImageDraw                                                
from PIL import ImageFont                                                

RST = 0                                                                  

# Créé un objet display - Create display object                          
disp = Adafruit_SSD1306.SSD1306_128_32(rst = RST)                          

# Initialise l'écran - init display                                      
disp.begin()                                                             

# Efface l'écran - Clear display.                                        
disp.clear()                                                             
disp.display()                                                           

# Créé un image avec un codage des couleurs sur 1 bit (noir et blanc)    
# Create blank image for drawing with mode '1' for 1-bit color.          
width = disp.width                                                       
height = disp.height                                                     
image = Image.new('1', (width, height))                                  

# On créé un objet sur lequel on va dessiner                             
# Get drawing object to draw on image.                                   
draw = ImageDraw.Draw(image)                                             
# Charge la font par défaut - load default font                          
#font = ImageFont.load_default()                                         
font = ImageFont.truetype(font="batmfa__.ttf", size = 15)                   
# On écrit du texte - Draw some text                                     
draw.text((0,0), 'Ouverture', font = font, fill = 255)                       
draw.text((0,16), 'Porte', font = font, fill = 255)                          

# Actualise l'affichage - Update display                                 
disp.image(image)                                                        
disp.display()                                                           