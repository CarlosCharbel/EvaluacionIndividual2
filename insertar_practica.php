<?php

require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function insertar_alumno($data){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();

    $id_alumno = $data["id_alumno"];
    $id_sistema = $data["id_sistema"];
    $numero_practica = $data["numero_practica"];
    
    $insert = "INSERT INTO practica (idalumno, idsistema, numero_practica) VALUES (:id_alumno, :id_sistema, :numero_practica);";

   $stmt = $link->prepare($insert);
   $stmt -> bindParam(":id_alumno",$id_alumno);
   $stmt -> bindParam(":id_sistema",$id_sistema);
   $stmt -> bindParam(":numero_practica",$numero_practica);


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