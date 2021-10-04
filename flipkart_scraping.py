import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.flipkart.com/search?q=iphone%2012&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html,'html.parser')


products_name=[]
products_original_price=[]
products_discount=[]
products_price=[]
products_display=[]
products_chip=[]
products_storage=[]
products_camera=[]

for a in soup.findAll('div', attrs={'class':'_3pLy-c row'}):
    
    name=a.find('div', attrs={'class':'_4rR01T'})
    specifications=a.findAll('li',attrs={'class':'rgWa7D'})
    product_price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    og_price=a.find('div', attrs={'class':'_3I9_wc _27UcVY'})
    discount=a.find('div', attrs={'class':'_3Ay6Sb'})
    
    
    product_storage=specifications[0].text
    display=specifications[1].text
    camera=specifications[2].text
    chip=specifications[3].text
    try:
        
        
        #print(og_price.text.encode("utf-8").decode("ascii","ignore"))
        #og_price=og_price.text.encode("utf-8").decode("ascii","ignore")
        #product_price=product_price.text.encode("utf-8").decode("ascii","ignore")
        
        products_name.append(name.text)
        products_original_price.append(og_price.text.encode("utf-8").decode("ascii","ignore"))
        products_discount.append(discount.text)
        products_price.append(product_price.text.encode("utf-8").decode("ascii","ignore"))
        products_storage.append(product_storage)
        products_display.append(display)
        products_camera.append(camera)
        products_chip.append(chip)
        
        
    except: 
        print("Error")
   

df= pd.DataFrame({'Product Name':products_name,'Original Price':products_original_price,'Discount':products_discount,'Discounted Price':products_price,'Storage':products_storage,'Display':products_display,'Camera':products_camera,'Chip':products_chip})

df.to_csv('flipkart.csv',encoding='utf-8')