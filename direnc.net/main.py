import direnc_extract_data
import pandas as pd

catagoriess_link, catagories_name = direnc_extract_data.catagories("https://www.direnc.net/kategori-konu-listesi","btn btn-default btn-upper")

i = 0
while(1):  
    new_url = catagoriess_link[i]
    price = []
    title = []
    img = []
    link = []
    while(1):  
        if new_url == catagoriess_link[i]: #this part for the first page of a catagory
           

            price, title, img, link = direnc_extract_data.products_properity("https://www.direnc.net/"+new_url, "currentPrice", "col col-12 productDescription", "imgInner", "productKapsa fl col-12")
            
            new_url = direnc_extract_data.page_numbers("https://www.direnc.net/"+new_url,"next") #for next pages url in the same catagory
            
        else: #starting from second page in the same catogry
            #print(new_url[0]) # it's a list 
            if not new_url:
                product = {'Price': price, 'Title': title, 'Img': img, 'Link': link}
                try:
                    exec("{} = pd.DataFrame(product, columns = ['Price', 'Title', 'Img', 'Link'])".format(catagories_name[i])) #creat our datafream for the first time
                    #exec("print({}.head)".format(catagories_name[i]))
                    exec("direnc_extract_data.save_csv(catagories_name[i],{})".format(catagories_name[i]))
                except:
                    print(catagories_name[i])
                    
                break

            temp_data = direnc_extract_data.products_properity("https://www.direnc.net"+new_url[0], "currentPrice", "col col-12 productDescription", "imgInner", "productKapsa fl col-12")
            price.extend(temp_data[0])
            title.extend(temp_data[1])
            img.extend(temp_data[2]) 
            link.extend(temp_data[3])
            new_url = direnc_extract_data.page_numbers("https://www.direnc.net"+new_url[0],"next") #and get the next pages urls
    print(i)
    i+=1





"""
DataFrames = []
i = 1
while(i<len(catagoriess)):
    a = catagoriess[i]
    a = a.replace(" ","_")
    a = a.replace("-","_")
    a = a.replace("3","uc")
    DataFrames.append(a)
    print(a)

    new_url = catagoriess[i]
    while(1):  
        if new_url == catagoriess[i]: #this part for the first page of a catagory
           

            price, title = direnc_extract_data.products_properity("https://www.direnc.net/"+new_url, "currentPrice", "col col-12 productDescription")

            product = {'Price': price, 
            'Title': title
            }

            exec("{} = pd.DataFrame(product, columns = ['Price', 'Title'])".format(a)) #creat our datafream for the first time
            

            new_url = direnc_extract_data.page_numbers("https://www.direnc.net/"+new_url,"next") #for next pages url in the same catagory

        elif not new_url:
            print(a.head())
            break
            
        else: #starting from second page in the same catogry
            #print(new_url[0]) # it's a list 

            price, title = direnc_extract_data.products_properity("https://www.direnc.net"+new_url[0], "currentPrice", "col col-12 productDescription")

            product = {'Price': price, 
            'Title': title
            }

            temp_df = pd.DataFrame(product, columns = ['Price', 'Title'])

            exec("{}={}.append(temp_df).reset_index(drop=True)".format(a, a))

            new_url = direnc_extract_data.page_numbers("https://www.direnc.net"+new_url[0],"next") #and get the next pages urls

    print(a,"sdafasdf")
    i+=2



print(arduino)
"""