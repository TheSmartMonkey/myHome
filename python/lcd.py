# coding: UTF-8                                                                                                      
import Adafruit_SSD1306                                                                                              

from PIL import Image                                                                                                
from PIL import ImageDraw                                                                                            
from PIL import ImageFont                                                                                            

# Créé un objet display - Create display object                                                                      
class LCD(object):                                                                                                   
    def __init__(self):                                                                                              
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst = None)                                                        

        self.disp.begin()                                                                                            
        self.disp.clear()                                                                                            
        self.disp.display()                                                                                          

    def displayText(self,line1,line2):                                                                               
        width = self.disp.width                                                                                      
        height = self.disp.height                                                                                    
        self.image = Image.new('1', (width, height))                                                                 

        self.draw = ImageDraw.Draw(self.image)                                                                       
        self.font = ImageFont.truetype(font = "batmfa__.ttf", size = 15)                                                  

        self.draw.text((0,0), line1, font = self.font, fill = 255)                                                       
        self.draw.text((0,16), line2, font = self.font, fill = 255)                                                      
        self.disp.image(self.image)                                                                                  
        self.disp.display()                                                                                          

if __name__=="__main__":                                                                                             
    from time import sleep                                                                                           
    lcd=LCD()                                                                                                        
    for message1,message2 in (("Ouverture","Porte"),("Porte","Ouverte"),("Fermeture","Porte"),("Porte","Fermée")):   
        lcd.displayText(message1, message2)                                                                           
        sleep(1)                                                                                                     