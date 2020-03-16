from PIL import Image
import time
from Functions import screenshot, get_window, key_press

c = 0
hwnd = get_window('VisualBoyAdvance')  
screenshot(hwnd)

Enter = 0x1C # Start
Z = 0x2C # A
J = 0x24 # Right
N = 0x31 # Down

while(True):
    
    
    key_press(Enter)
    
    for i in range(3):
        time.sleep(.1)
        key_press(Z)
    
    time.sleep(1.)
    key_press(Z)
    
    time.sleep(1.)    
    
    screenshot(hwnd)
    
    im = Image.open('screen.bmp')
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((365, 140))
    
    if(r==246): # if we have a red magikarp
        
        key_press(Z)
        time.sleep(1.)
        
        key_press(J)
        time.sleep(.1)
        
        key_press(N)
        time.sleep(.1)
        
        for i in range(2):
            key_press(Z)
            time.sleep(.2)
        
        time.sleep(1.)
        
        c += 1
        print('{} red Magikarp encountered.'.format(c))
        
        
    else: # if we have not a red magikarp
        
        if(r!=152 and b!=192): # maybe we have not fished anything
            r, g, b = rgb_im.getpixel((365, 250)) # additional check for the fat man
            if(r!=112 and b!=160):
                break # we have fished a magikarp wich is not red!