<?php

require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function insertar_alumno($data){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();

    $nombre = $data["nombre"];
    $matricula = $data["matricula"];
    $grupo = $data["grupo"];
    
    $insert = "INSERT INTO alumno (nombre, matricula, grupo) VALUES (:nombre, :matricula, :grupo);";

   $stmt = $link->prepare($insert);
   $stmt -> bindParam(":nombre",$nombre);
   $stmt -> bindParam(":matricula",$matricula);
   $stmt -> bindParam(":grupo",$grupo);


   if ($stmt -> execute())
   {
    echo "Uploaded Succesfully!";
   }
   
   return 1;
}

  $json = file_get_contents('php://input');
  $data = json_decode($json,true);
  insertar_alumno($data);
  
?>