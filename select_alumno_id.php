<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_alumno_id($id_alumno){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


   $select = "SELECT nombre from alumno where idalumno = " .$id_alumno;


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$id_alumno = $_GET['id'];

$result = get_alumno_id($id_alumno);

echo json_encode($result);

?>