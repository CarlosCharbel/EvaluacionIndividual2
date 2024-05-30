<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_sistema(){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


    $select = "SELECT idsistema,p1,p2,p3 from sistema";


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$result = get_sistema();

echo json_encode($result);

?>