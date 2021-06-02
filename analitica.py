import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import time

df = pd.read_csv('covid 2.csv',sep=';', header=0) 
cabecera = ["Fiebre","Cansancio","Tos","Ahogo","Dolorgarganta","Dolor","Congestion","Goteo","Diarrea","Infante","Menor","Joven","Adulto","Mayor","Mujer","Hombre","Trans","CS","CN","CNS","Resultado"] 
df.columns = cabecera 
df.head()

df.drop(["Trans"],axis=1,inplace=True)
df.head()

x1 = df.values[:,0]
x2 = df.values[:,1]
x3 = df.values[:,2]
x4 = df.values[:,3]
x5 = df.values[:,4]
x6 = df.values[:,5]
x7 = df.values[:,6]
x8 = df.values[:,7]
x9 = df.values[:,8]
x10 = df.values[:,9]
x11 = df.values[:,10]
x12 = df.values[:,11]
x13 = df.values[:,12]
x14 = df.values[:,13]
x15 = df.values[:,14]
x16 = df.values[:,15]
x17 = df.values[:,16]
x18 = df.values[:,17]
x19 = df.values[:,18]
y = df.values[:,19]
x0 = np.ones(x1.shape)

X = np.matrix([x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19]).T
features = np.matrix([x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19])
Y = np.matrix (y).T
labels = np.matrix (y)
X.shape

NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/1.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z1=[]
for x in field_1:
   z1.append(x['field1'])
z1=z1[1]
z1=int(z1)


NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/2.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z2=[]
for x in field_1:
   z2.append(x['field2'])
z2=z2[1]
z2=int(z2)
 

NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/3.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z3=[]
for x in field_1:
   z3.append(x['field3'])
z3=z3[1]
z3=int(z3)


NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/4.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z4=[]
for x in field_1:
   z4.append(x['field4'])
z4=z4[1]
z4=int(z4)
  

NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/5.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z5=[]
for x in field_1:
   z5.append(x['field5'])
z5=z5[1]
z5=int(z5)
   

NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/6.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z6=[]
for x in field_1:
   z6.append(x['field6'])
z6=z6[1]
z6=int(z6)
     

NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/7.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z7=[]
for x in field_1:
   z7.append(x['field7'])
z7=z7[1]
z7=int(z7)


NEW_URL = 'https://api.thingspeak.com/channels/1402727/fields/8.json?api_key=4ULGHLRFIKX30FU8&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z8=[]
for x in field_1:
   z8.append(x['field8'])
z8=z8[1]
z8=int(z8)
   

NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/1.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z9=[]
for x in field_1:
   z9.append(x['field1'])
z9=z9[1]
z9=int(z9)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/2.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z10=[]
for x in field_1:
   z10.append(x['field2'])
z10=z10[1]
z10=int(z10)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/3.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z11=[]
for x in field_1:
   z11.append(x['field3'])
z11=z11[1]
z11=int(z11)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/4.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z12=[]
for x in field_1:
   z12.append(x['field4'])
z12=z12[1]
z12=int(z12)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/5.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z13=[]
for x in field_1:
   z13.append(x['field5'])
z13=z13[1]
z13=int(z13)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/6.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z14=[]
for x in field_1:
   z14.append(x['field6'])
 z14=z14[1]
 z14=int(z14)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/7.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z15=[]
for x in field_1:
   z15.append(x['field7'])
z15=z15[1]
z15=int(z15)


NEW_URL = 'https://api.thingspeak.com/channels/1402728/fields/8.json?api_key=7T4EMCJHQ6TTCYD2&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z16=[]
for x in field_1:
   z16.append(x['field8'])
z16=z16[1]
z16=int(z16)


NEW_URL = 'https://api.thingspeak.com/channels/1402729/fields/1.json?api_key=MV3TJWU6TZQCIV4O&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z17=[]
for x in field_1:
   z17.append(x['field1'])
z17=z17[1]
z17=int(z17)


NEW_URL = 'https://api.thingspeak.com/channels/1402729/fields/2.json?api_key=MV3TJWU6TZQCIV4O&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z18=[]
for x in field_1:
   z18.append(x['field2'])
z18=z18[1]
z18=int(z18)


NEW_URL = 'https://api.thingspeak.com/channels/1402729/fields/3.json?api_key=MV3TJWU6TZQCIV4O&results=2'

get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
z19=[]
for x in field_1:
   z19.append(x['field3'])
z19=z19[1]
z19=int(z19)


z0=1
X1=np.array([z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19]).reshape(1,-1)
prediccion = clf.predict(X1)
print(prediccion)

NEW_URL = 'https://api.thingspeak.com/channels/1344250/fields/3.json?api_key=SKF96HHC05WSCCXA&results=2'
 
get_data = requests.get(NEW_URL).json()

channel_id=get_data['channel']['id']
field_1=get_data['feeds']
T=[]
for x in field_1:
   T.append(x['field3'])
T=T[1]
T=float(T)


NEW_URL1 = 'https://api.thingspeak.com/channels/1344250/fields/5.json?api_key=SKF96HHC05WSCCXA&results=2'

get_data1 = requests.get(NEW_URL1).json()

channel_id=get_data1['channel']['id']
field_5=get_data1['feeds']
P=[]
for x in field_5:
   P.append(x['field5'])
P=P[1]
P=float(P)


NEW_URL2 = 'https://api.thingspeak.com/channels/1344250/fields/7.json?api_key=SKF96HHC05WSCCXA&results=2'

get_data2 = requests.get(NEW_URL2).json()

channel_id=get_data2['channel']['id']
field_7=get_data2['feeds']
O=[]
for x in field_7:
   O.append(x['field7'])
O=O[1]
O=float(O)
    
if(prediccion==1 and T<37.5 and P<130 and O>=90):
     C=1
if((prediccion==1 and ((T>=37.5 and T<38.5) or (O<90 and O>=87) or (P>=130 and P<300))) or (prediccion==0 and T<37.5 and P<130 and O>=90)):
     C=2
if(prediccion==0 and ((T>=37.5 and T<39.5) or (O<90 and O>=84))):
     C=3
if(O<83 or P>=300 or P<=30 or T>=39.5):
     C=4
print(C)
enviar = requests.get("https://api.thingspeak.com/update?api_key=6TSBI19FP6L81E62&field8="+str(C))
