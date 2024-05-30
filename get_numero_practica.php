<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_numero_practica(){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


    $select = "SELECT numero_practica from practica";


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$result = get_numero_practica();

echo json_encode($result);

?>