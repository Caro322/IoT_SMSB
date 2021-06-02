import smbus #Proporciona acceso desde python al driver I2C de linux
import time #Conjunto de funciones para trabajar con tiempos
import paho.mqtt.publish as publish #Librería de MQTT
import max30102 #Importa el archivo donde se guardan ls direcciones del sensor max30102
import hrcalc #Importa el archivo donde se realiza la lectura del sensor max30102
import requests #Permite enviar los datos con el protocolo HTTP
import RPi.GPIO as GPIO
from datetime import datetime #Permite hacer operaciones con fechas y horas
from time import sleep #Permite detener la ejecución del programa por unos segundos

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

channelID = "1344250" #ID del canal de thingspeak

apikey = "6TSBI19FP6L81E62" #Apikey del canal de thingspeak


useUnsecuredTCP= False #Se especifica que no se utilizará TCP

useUnsecuredWebsockets = False #Se especifica que no se utilizaran los unsecured web sockets

useSSLWebsockets = True #Se especifica que se utilizarán los web sockets con capa de seguridad

mqttHost = "mqtt.thingspeak.com" #Se declara el host al que se le enviarán los mensajes


if useUnsecuredTCP: #Especificaciones de TCP
    tTransport = "tcp" #Transporte e tipo TCP
    tport = 1883 #Usa el puerto 1883
    tTLS = None #Sin capa de seguridad de transporte
   
if useUnsecuredWebsockets: #Especificaciones de unsecured web sockets
    tTransport = "websockets" #Transporte de tipo web sockets
    tPort = 80 #Usa el puerto 80
    tTLS = None #Sin capa de seguridad de transporte
   
if useSSLWebsockets: #Especificaciones de SSL web sockets
    import ssl #Importa la librería de capa de seguridad
    tTransport = "websockets" #Transporte de tipo web sockets
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    #Configuración de la capa de seguridad
    tPort = 443 #Usa el puerto 443
   
topic = "channels/" + channelID + "/publish/" + apikey #Indica el topic en el que se publicarán
#los mensajes
   
m=max30102.MAX30102() #Indica la dirección del sensor max30102

class MLX90614(): #Indica las direcciones del mlx90614
    MLX90614_RAWIR1=0x04
    MLX90614_RAWIR2=0x05
    MLX90614_TA=0x06
    MLX90614_TOBJ1=0x07
    MLX90614_TOBJ2=0x08
    MLX90614_TOMAX=0x20
    MLX90614_TOMIN=0x21
    MLX90614_PWMCTRL=0x22
    MLX90614_TARANGE=0x23
    MLX90614_EMISS=0x24
    MLX90614_CONFIG=0x25
    MLX90614_ADDR=0x0E
    MLX90614_ID1=0x3C
    MLX90614_ID2=0x3D
    MLX90614_ID3=0x3E
    MLX90614_ID4=0x3F
    comm_retries = 5
    comm_sleep_amount = 0.1
    def __init__(self, address=0x5a, bus_num=1): #Especifica detalles de dirección y del bus
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)
    def read_reg(self, reg_addr): #Lee los datos del sensor
        err = None
        for i in range(self.comm_retries):
            try:
                return self.bus.read_word_data(self.address, reg_addr)
            except IOError as e:
                err = e
               
                sleep(self.comm_sleep_amount) #Evita problemas con el sensor cuando lee
                #Demasiado rápido
        raise err
    def data_to_temp(self, data): #Función de converción
        temp = (data*0.02) - 273.15 #Convierte los datos a grados celcius
        return temp
    def get_amb_temp(self): #Lectura de la temperatura ambiente
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)
    def get_obj_temp(self): #Lectura de la temperatura del objeto
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)
if __name__ == "__main__": #Verifica si el módulo ha sido ejecutado o no
     while(1): #Bucle infinito
       sensor = MLX90614() #Llama a las direcciones del sensor
       ta=sensor.get_amb_temp() #Valor de la temperatura ambiente
       to=sensor.get_obj_temp() #Valor de la temperatura del objeto
       print("La temperatura ambiente es:",ta) #Imprime la temperatura ambiente
       print("Tu temperatura es:",to) #Imprime la temperatura del objeto
       time.sleep(1) #Delay de 1 seg
       red, ir = m.read_sequential() #Lectura del sensor pulsoxímetro
       h=hrcalc.calc_hr_and_spo2(ir,red) #Almacenamiento de datos del sensor pulsoxímetro
       if (h[0]==(-999)): #Si recibe el valor de -999
          p=0 #El valor almacenado para la frecuencia cardiaca será 0
       else: #Si no
          p=h[0] #Se almacenará el valor de h en la primera posición
       if (h[2]==(-999)): #Si recibe el valor de -999
          o=0 #El valor almacenado para la saturación de oxígeno en sangre será 0
       else: #Si no
          o=h[2] #Se almacenará el valor de h en la tercera posición
       print("Tu ritmo cardiaco es:",p) #Se imprime la frecuencia cardiaca
       print("Tu saturación de oxigeno en sangre es:",o) #Se imprime la saturación de oxigeno
       #en sangre
       now=datetime.now() #Se guarda el momento actual
       td = datetime.timestamp(now) #Se guarda la semilla del momento actual
       ts = datetime.fromtimestamp(td) #Se obtiene la fecha y la hora actual
       IDT="T" #ID del sensor de temperatura
       IDO="O" #ID del sensor de oxígeno
       IDP="P" #Id del sensor de pulso
       
       tPayload1 = "field1="+str(ts)+"&field2="+IDT+"&field3="+str(to)+"&field4="+IDP+"&field5="+str(p)+"&field6="+IDO+"&field7="+str(o)
       #Mensaje que será enviado utilizando el protocolo MQTT    
       publish.single(topic, payload=tPayload1, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
       #Publicación del mensaje utilizando todos los parámetos especificados anteriormente
       if(o<83 or p>=300 or p<=30 or to>=39.5):
           GPIO.output(11, True)
           time.sleep(0.5)
       else:
           GPIO.output(11, False)

       #enviar = requests.get("https://api.thingspeak.com/update?api_key=6TSBI19FP6L81E62&field1="+str(to)+"&field2="+str(o)+"&field3="+str(p))
       #Envío de datos con protocolo HTTP
