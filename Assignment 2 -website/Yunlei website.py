import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt


response = requests.get("https://www.hko.gov.hk/tide/MWCtextPH2026_uc.htm")  #request the website
#if response.ok:
    #print("data available")  #check if it is available to request the website
#else:
    #print("data fail")
content = response.text  #get the text type data
soup = BeautifulSoup(content,"html.parser")
prehighData = []  #create a list
all_prehigh = soup.findAll("td")  #Get all the data with the tag"td"

for prehigh in all_prehigh :  #use loop to get all the data
    prehighNumber = prehigh.string
    if prehighNumber != None and prehighNumber[0] == " " :
        prehighData.append(float(prehighNumber.strip()))
        

for i in range(0, 31):
    prehighData [i] = prehighData[24*i] #get the data of the first hour

prehighData = prehighData[:31*1] #get the data of the first month
Height = np.array(prehighData).reshape(1,31)

#print(Height[0])
#print (len(prehighData))       Check the data correct or not
#print (prehighData)

x=1+np.arange(31)
y=Height[0]

fig, ax = plt.subplots()
rects=ax.bar(x, y, width=0.75, edgecolor="black", linewidth=0.7,color="#756477") #set the bar
ax.bar_label(rects,padding=3)

ax.set(xlim=(0, 32), xticks=np.arange(1, 32), #set the x and y data arange
       ylim=(0, 3), yticks=np.arange(1, 3))


#set some chart message and background color
ax.set_title("Predicted heights of tides at Ma Wan in January 2026") 
ax.set_xlabel("Date(Jan)")
ax.set_ylabel("Height(m)")
ax.set_facecolor("#F6EFE9")
plt.show()



