<?php

require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function insertar_alumno($data){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();

    $p1 = $data["p1"];
    $p2 = $data["p2"];
    $p3 = $data["p3"];
    
    $insert = "INSERT INTO sistema (p1, p2, p3) VALUES (:p1, :p2, :p3);";

   $stmt = $link->prepare($insert);
   $stmt -> bindParam(":p1",$p1);
   $stmt -> bindParam(":p2",$p2);
   $stmt -> bindParam(":p3",$p3);


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