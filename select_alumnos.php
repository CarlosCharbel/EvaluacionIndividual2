<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_alumnos(){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


    $select = "SELECT idalumno,nombre,matricula,grupo from alumno";


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$result = get_alumnos();

echo json_encode($result);

?>



