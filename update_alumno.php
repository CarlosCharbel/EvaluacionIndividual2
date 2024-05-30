<?php

require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function update_alumno($data){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();

    $nombre = $data["nombre"];
    $matricula = $data["matricula"];
    $grupo = $data["grupo"];
    $id_alumno = $data["id_alumno"];
    

    $update = "UPDATE alumno SET grupo = :grupo, matricula = :matricula, nombre = :nombre WHERE idalumno = :idalumno;";

    $stmt = $link->prepare($update);
    $stmt -> bindParam(":grupo",$grupo);
    $stmt -> bindParam(":matricula",$matricula);
    $stmt -> bindParam(":nombre",$nombre);
    $stmt -> bindParam(":idalumno",$id_alumno);

    if ($stmt -> execute())
    {
        echo "Updated Alumno: " .$nombre. " Succesfully!";
    }
   
   return 1;
}

  $json = file_get_contents('php://input');
  $data = json_decode($json,true);
  update_alumno($data);
  
?>