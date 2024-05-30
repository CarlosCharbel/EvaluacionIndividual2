<?php

require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function update_alumno($data){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();

    $p1 = $data["p1"];
    $p2 = $data["p2"];
    $p3 = $data["p3"];
    $id_sistema = $data["id_sistema"];
    
    $update = "UPDATE sistema SET p1 = :p1, p2 = :p2, p3 = :p3 WHERE idsistema = :idsistema;";

    $stmt = $link->prepare($update);
    $stmt -> bindParam(":p1",$p1);
    $stmt -> bindParam(":p2",$p2);
    $stmt -> bindParam(":p3",$p3);
    $stmt -> bindParam(":idsistema",$id_sistema);

    if ($stmt -> execute())
    {
        echo "Updated Sistema: " .$id_sistema. " Succesfully!";
    }
   
   return 1;
}

  $json = file_get_contents('php://input');
  $data = json_decode($json,true);
  update_alumno($data);
  
?>