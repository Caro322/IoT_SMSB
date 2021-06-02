<?php //Inicio del archivo php
$Nombre=$_POST['Nombre']; //Se almacena el nombre ingresado por el usuario al registrarse
$Apellido=$_POST['Apellido']; //Se almacena el apellido ingresado por el usuario al registrarse
$Email=$_POST['inputEmail4']; //Se almacena el email ingresado por el usuario al registrarse
$Password=$_POST['inputPassword4']; //Se almacena la contraseña ingresado por el usuario al registrarse
$Codigo=$_POST['inputAddress']; //Se almacena el código ingresado por el usuario al registrarse
$Genero=$_POST['flexRadioDefault']; //Se almacena el género ingresado por el usuario al registrarse
$Prueba=$_POST['gridCheck']; //Se almacena el resultado de la prueba ingresado por el usuario al registrarse
$conn= new mysqli('fdb27.125mb.com','3784927_smsbuser','mi36basededatos24','3784927_smsbuser');
if($conn->connect_error){
 die('Connection Failed : ' . $conn->connect_error); //Si hay un error de conexión recibiremos la información del error
}else{
        $stmt = $conn->prepare("insert into user(Nombre,Apellido,Email,Password,Genero,Codigo,Prueba) 
         values(?,?,?,?,?,?,?)"); //Incerta en la base de datos los datos ingresados por el usuario
        $stmt->bind_param("ssssiii",$Nombre,$Apellido,$Email,$Password,$Genero,$Codigo,$Prueba); /*Enlaza las variables a los marcadores
        de parámetros*/
        $stmt->execute(); //Se ejercuta el insertar los datos en la base de datos
        echo ("Has sido registrado, disfruta tu smart band"); //Se imprime un mensaje para que el usuario sepa que todo salió bien
        $conn->close(); //Se cierra la conexión
         echo "Gracias por registarte" . " -" . "<meta http-equiv='refresh' content='0; URL=http://savemesmartband.125mb.com/iniciarsesion.html'>";
         //Se redirige al usuario a la página de inicio
} 

?> <!-- Fin del archivo php-->