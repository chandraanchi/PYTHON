
# '''webscraping'''

# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# '''request to allow website for web scarping'''
# req=requests.get("https://www.flipkart.com/search?q=realme+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")
# # print(req)     #if you get response code 200 to success 

# soup=BeautifulSoup(req.content,"html.parser")   #for webscarppng
# # print(soup)

# '''mobile name scrapping'''
# mobile_names=soup.find_all("div",class_="_4rR01T")
# # print(mobile_names)

# names=[]
# for i in mobile_names:
#     d=i.get_text()
#     names.append(d)
# # print(names)

# '''price scrapping'''
# price=soup.find_all("div",class_="_30jeq3 _1_WHN1")
# # print(price)

# prices=[]
# for i in price:
#     d=i.get_text()
#     s=d[1:]
#     prices.append(s)
# # print(prices)

# '''ratings'''
# ratings=soup.find_all("div",class_="_3LWZlK")
# # print(ratings)

# rating=[]
# for i in ratings:
#     d=float(i.get_text())
#     rating.append(d)
# # print(rating)

# '''images scarapping'''
# images=soup.find_all("img",class_="_396cs4")
# # print(images)

# image=[]
# for i in images:
#     d=i["src"]
#     image.append(d)
# # print(image)

# '''links scraping'''
# links=soup.find_all("a",class_="_1fQZEK")
# # print(links)
# link=[]
# for i in links:
#     d=i["href"]
#     link.append(d)
# # print(link)

# '''pandas use'''
# df=pd.DataFrame()
# # print(df)
# df['mobile_names']=names
# df['price']=prices
# df['ratings']=rating
# df['images']=image
# df['links']=link
# print(df)



''''''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# response=requests.get("https://www.flipkart.com/search?q=samsung%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# # print(response)

# soup=BeautifulSoup(response.content,"html.parser")
# # print(soup)

# samnames=soup.find_all("div",class_="_4rR01T")
# # print(samnames)

# names=[]
# for n in samnames:
#     n.get_text()
#     names.append(n)
# print(names)
# print( )

# samprices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
# # print(samprices)

# price=[]
# for i in samprices:
#     i.get_text()    
#     price.append(i)
# print(price)

# df=pd.DataFrame()
# # print(df)
# df['sanames']=names
# df[samprices]=price
# print(df)