from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
ratingarr=[]
ratingz=[]
choice=0
a1=0
a=0
while(choice!=4):
    print("1.DO YOU WANT TO SEE PRODUCTS PREVAILING IN FLIPKART?")
    print("2.DO YOU WANT TO SEE PRODUCTS PREVAILING IN SNAPDEAL?")
    print("3.DO YOU WANT TO SEE WHICH E-SITE IS EFFICIENT?")
    print("4.EXIT")
    print("***********************************************************************")
    choice=int(input())
    
        
    if(choice==1):
        i=0
        print("NOW YOU ARE IN FLIPKART")
        my_url='https://www.flipkart.com/search?q=kurti&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        uClient=uReq(my_url)
        page_html=uClient.read()
        uClient.close()
        page_soup=soup(page_html,"html.parser")
        containers=page_soup.findAll("div",{"class":"_3liAhj _1R0K0g"})
        print("total number of dresses in this page:",len(containers))
        container=containers[0]
        for container in containers:
            name1=container.findAll("a",{"class":"_2cLu-l"})
            name=name1[0].text.strip()
            print(name)
            price1=container.findAll("div",{"class":"_1vC4OE"})
            price=price1[0].text.strip()
            print(price)
            rat1=container.findAll("span",{"class":"_2_KrJI"})
            try:
                rat=rat1[0].text
                if(rat=="4 ★"or rat=="5 ★" or rat=="3 ★"or rat=="2 ★" or rat=="1 ★"):
                    print("rating:",rat[:2])
                    ratingarr.append(float(rat[:2]))
                    i+=1
                else:
                    print("rating:",rat[:3])
                    ratingarr.append(float(rat[:3]))
                    i+=1
        
            except IndexError:
                print("no ratings available")
        a=(sum(ratingarr)/i)
        
    
    if(choice==2):
        i=0
        print("NOW YOU ARE IN SNAPDEAL")
        my_url='https://www.snapdeal.com/search?keyword=kurti&santizedKeyword=&catId=178&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
        uClient=uReq(my_url)
        page_html=uClient.read()
        uClient.close()
        page_soup=soup(page_html,"html.parser")
        containers=page_soup.findAll("div",{"class":"product-tuple-description"})
        #print(soup.prettify(containers[0])) noooo needddd!!!hahahaha 
        print(len(containers))
        container=containers[0]
        for container in containers:
            price1=container.findAll("div",{"class":"lfloat marR10"})
            price=price1[0].text.strip()
            print(price)
            name1=container.findAll("p",{"class":"product-title"})
            name=name1[0].text.strip()
            print(name)
            rat1=container.findAll('a')
            rat=rat1[0]
            linkz=rat.get('href')
            uClient1=uReq(linkz)
            page_html1=uClient1.read()
            uClient1.close()
            page_soup1=soup(page_html1,"html.parser")
            containers1=page_soup1.findAll("div",{"class":"pdp-e-i-ratereviewQA marT10"})
            container1=containers1[0]
    
            for container1 in containers1:
                rating1=container1.findAll("span",{"class":"avrg-rating"})
                try:
                    rating=rating1[0].text.strip()
                    print("rating:",rating)
                    ratingz.append(float(rating[1:4]))
                    i+=1
                except IndexError:
                    print("no ratings available")
        a1=(sum(ratingz)/i)
        
    if(choice==3):
        print("OVERALL FLIPKART RATING:")
        print("%.2f" % round(a,2))
        print("OVERALL SNAPDEAL RATING:")
        print("%.2f" % round(a1,2))
        if(a>a1):
            print("YOU CAN SHOP IN FLIPKART")
        else:
            print("YOU CAN SHOP IN SNAPDEAL")
    if(choice==4):
        break
            
        
        
    
