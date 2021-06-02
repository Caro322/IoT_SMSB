<?php //Inicio del archivo php
$conn= new mysqli('fdb27.125mb.com','3784927_smsbuser','mi36basededatos24','3784927_smsbuser'); /*Se crea la conexión especificando el
host, el nombre de usuario, la contraseña y la base de datos a la cual se desea conectar*/

session_start();

$Usuario = $_POST['floatingInput']; //Se almacena el usuario ingresado por el usuario al iniciar sesión
$Pass = $_POST['floatingPassword']; //Se almacena la contraseña ingresada por el usuario al iniciar sesión 

$_SESSION['floatingInput']=$Usuario;

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error); //Si hay un error de conexión recibiremos la información del error
}

 

$sql = "SELECT * FROM user where Email='".$Usuario."' and Password='".$Pass."'"; /*Selecciona el email y la contraseña guardadas en la base
de datos*/
$result = $conn->query($sql);//Ejecuta la selección de la base de datos usser
$var =1; //Se inicializa var en 1
$counter=0; //Se inicializa en contador en cero
$nombres; //Se declara la variable donde se almacenará el nombre del usuario
$apellidos; //Se declara la variable donde se almacenará el apellido del usuario
if ($result->num_rows > 0) {
  /* Retorna el número de filas del resultado, este debe ser mayor a cero si los datos ingresados y los almacenados en la base de
  datos coinciden*/
  echo "Disfruta tu smart band" . " -" . "<meta http-equiv='refresh' content='0; URL=http://savemesmartband.125mb.com/inicio.html'>"; 
  //Redirige al usuario a la página de inicio
  while($row = $result->fetch_assoc() ) {
  //Retorna un arreglo asociativo correspondiente a la fila obtenida
    //if($counter==1){
    //Sirve para saltarme el primer resultado 
                    $nombres=$row["Nombre"]; //Se almacena el nombre del usuario
                    $apellidos=$row["Apellido"]; 
    //}
    //$counter=$counter+1;
  }
} else {
  echo "Usuario o contraseña incorrecta intentar de nuevo" . " -" . "<meta http-equiv='refresh' content='0; URL=http://savemesmartband.125mb.com/Ingresa.html'>";
  ?>
  <div class="alert alert-danger d-flex justify-content-center" role="alert">
  Error al iniciar sesión
</div>
  <?php
}

 

$conn->close();

?>

<script type="text/javascript">
const name = "<?php echo $nombres; ?>";
const surname = "<?php echo $apellidos; ?>";

 

alert( "Bienvenido "+ name + " "+surname );
    // to set into local storage
    /* localStorage.setItem("NAME", name);
    localStorage.setItem("SURNAME", surname); */
    
    sessionStorage.setItem("NAME", name);
    sessionStorage.setItem("SURNAME", surname);
</script>