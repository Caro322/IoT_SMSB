<?php //Inicio del archivo php
$Fiebre=$_POST['Fiebre']; //Se almacena el dato ingresado por el usuario
$Cansancio=$_POST['Cansancio']; //Se almacena el dato ingresado por el usuario
$Tos=$_POST['Tos']; //Se almacena el dato ingresado por el usuario
$Ahogo=$_POST['Ahogo']; //Se almacena el dato ingresado por el usuario
$Dolorgarganta=$_POST['Dolorgarganta']; //Se almacena el dato ingresado por el usuario
$Dolorcuerpo=$_POST['Dolorcuerpo']; //Se almacena el dato ingresado por el usuario
$Congestion=$_POST['Congestion']; //Se almacena el dato ingresado por el usuario
$Goteo=$_POST['Goteo']; //Se almacena el dato ingresado por el usuario
$Diarrea=$_POST['Diarrea']; //Se almacena el dato ingresado por el usuario
$Infante=$_POST['Infante']; //Se almacena el dato ingresado por el usuario
$Menor=$_POST['Menor']; //Se almacena el dato ingresado por el usuario
$Joven=$_POST['Joven']; //Se almacena el dato ingresado por el usuario
$Adulto=$_POST['Adulto']; //Se almacena el dato ingresado por el usuario
$Mayor=$_POST['Mayor']; //Se almacena el dato ingresado por el usuario
$Femenino=$_POST['Femenino']; //Se almacena el dato ingresado por el usuario
$Masculino=$_POST['Masculino']; //Se almacena el dato ingresado por el usuario
$Transgenero=$_POST['Transgenero']; //Se almacena el dato ingresado por el usuario
$Contactosi=$_POST['Contactosi']; //Se almacena el dato ingresado por el usuario
$Contactono=$_POST['Contactono']; //Se almacena el dato ingresado por el usuario
$Contactonosabe=$_POST['Contactonosabe']; //Se almacena el dato ingresado por el usuario
$Pais=$_POST['Pais']; //Se almacena el dato ingresado por el usuario

 

 

$conn= new mysqli('fdb27.125mb.com','3784927_smsbuser','mi36basededatos24','3784927_smsbuser'); /*Se crea la conexión especificando el
host, el nombre de usuario, la contraseña y la base de datos a la cual se desea conectar*/
if($conn->connect_error){
 die('Connection Failed : ' . $conn->connect_error); //Si hay un error de conexión recibiremos la información del error
}else{
        $stmt = $conn->prepare("insert into sintomas(Fiebre,Cansancio,Tos,Ahogo,Dolorgarganta,Dolorcuerpo,Congestion,Goteo,Diarrea,Infante,Menor,Joven,Adulto,Mayor,Femenino,Masculino,Transgenero,Contactosi,Contactono,Contactonosabe,Pais) 
         values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"); //Incerta en la base de datos los datos ingresados por el usuario
        $stmt->bind_param("iiiiiiiiiiiiiiiiiiiis",$Fiebre,$Cansancio,$Tos,$Ahogo,$Dolorgarganta,$Dolorcuerpo,$Congestion,$Goteo,$Diarrea,$Infante,$Menor,$Joven,$Adulto,$Mayor,$Femenino,$Masculino,$Transgenero,$Contactosi,$Contactono,$Contactonosabe,$Pais);
        /*Enlaza las variables a los marcadores de parámetros*/
        $stmt->execute(); //Se ejercuta el insertar los datos en la base de datos
        echo (""); //Se imprime un mensaje para que el usuario sepa que todo salió bien
        $conn->close(); //Se cierra la conexión
        echo "Gracias por reesponder" . " -" . "<meta http-equiv='refresh' content='0; URL=http://savemesmartband.125mb.com/Salud.html'>";
        //Se redirige al usuario a la página de consejos
}

?> <!-- Fin del archivo php-->