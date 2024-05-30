<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_practica(){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


    $select = "SELECT idlab,idalumno,idsistema,numero_practica from practica";


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$result = get_practica();

echo json_encode($result);

?>