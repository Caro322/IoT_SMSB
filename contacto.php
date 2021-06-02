<?php //Inicio del archivo php
$Nombre=$_POST['name']; //Se almacena el nombre ingresado por el usuario al registrarse
$Email=$_POST['email']; //Se almacena el email ingresado por el usuario al registrarse
$Mensaje=$_POST['message']; //Se almacena la contraseña ingresado por el usuario al registrarse

$conn= new mysqli('fdb27.125mb.com','3784927_smsbuser','mi36basededatos24','3784927_smsbuser');
if($conn->connect_error){
 die('Connection Failed : ' . $conn->connect_error); //Si hay un error de conexión recibiremos la información del error
}else{
        $stmt = $conn->prepare("insert into contacto(Nombre,Email,Mensaje) 
         values(?,?,?)"); //Incerta en la base de datos los datos ingresados por el usuario
        $stmt->bind_param("sss",$Nombre,$Email,$Mensaje); /*Enlaza las variables a los marcadores
        de parámetros*/
        $stmt->execute(); //Se ejercuta el insertar los datos en la base de datos
        echo (""); //Se imprime un mensaje para que el usuario sepa que todo salió bien
        $conn->close(); //Se cierra la conexión
         echo "Gracias por tu mensaje" . " -" . "<meta http-equiv='refresh' content='0; URL=http://savemesmartband.125mb.com/Contactanos.html'>";
         //Se redirige al usuario a la página de inicio
} 