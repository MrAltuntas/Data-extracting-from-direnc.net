from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os 

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')


PATH = os.path.dirname(os.path.realpath(__file__)) + "\chromedriver.exe"
driver = webdriver.Chrome(executable_path = PATH,chrome_options=options)


def catagories(urll, classs):
    catagories_name=[]
    catagories_link=[]
    driver.get(urll)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    for a in soup.findAll('a', class_=classs):
        catagories_name.append(a.text)
        catagories_link.append(a['href'])

    for i in range(len(catagories_name)):
        catagories_name[i] = catagories_name[i].replace(" ","_")
        catagories_name[i] = catagories_name[i].replace("-","_")
        catagories_name[i] = catagories_name[i].replace("3","uc")
    return catagories_link,catagories_name

def page_numbers(urll,classs):
    pages=[]
    driver.get(urll)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    for a in soup.findAll('a', class_=classs):
        try:
            pages.append(a['href'])
        except:
            print()
    #print(type(pages),pages)
    return pages

def products_properity(urll, clas_price, clas_title,clas_img,clas_link):
    products_price=[]
    products_title=[]
    products_img=[]
    products_link = []
    driver.get(urll)

    driver.execute_script("window.scrollTo(0, 10000)") 

    sleep(1)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    for a in soup.findAll('span', class_=clas_price):
        try:
            #print(a.text)
            products_price.append(a.text)
        except:
            print()

    for a in soup.findAll('a', class_=clas_title):
        try:
            #print(a.text)
            products_title.append(a.text)
        except:
            print()

    img_tags = soup.findAll('span', class_=clas_img)
    for a in img_tags:
        try:
            products_img.append(a.find('img')['src'])
        except:
            print()

    img_tags = soup.findAll('div', class_=clas_link)
    for a in img_tags:
        try:
            #print(a.text)
            products_link.append(a.find('a')['href'])
        except:
            print()

    return products_price, products_title, products_img, products_link


def save_csv(name, df):
    print(name)
    print(df)
    name = name + ".csv"
    df.to_csv(r'C:\Users\Arflok\Desktop\web\extracting data\ '+name, index=False, encoding='utf-8')



"""
exec("{} = {}.append({'Price': products_price('https://www.direnc.net'+new_url[0],'currentPrice')}, ignore_index=True)".format(a))
            exec("{} = {}.append({'Title': products_title('https://www.direnc.net'+new_url[0],'col col-12 productDescription')}, ignore_index=True)".format(a))



  product = {'Price': products_price("https://www.direnc.net/"+catagoriess[i],"currentPrice"), 
                'Title': products_title("https://www.direnc.net/"+catagoriess[i],"col col-12 productDescription")
    }
exec("{} = pd.DataFrame(product, columns = ['Price', 'Title'])".format(a))
    exec("print({}.head)".format(a))

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')"""