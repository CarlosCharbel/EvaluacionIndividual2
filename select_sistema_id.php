<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_sistema_id($id_sistema){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


   $select = "SELECT p1,p2,p3 from sistema where idsistema = " .$id_sistema;


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$id_sistema = $_GET['id'];

$result = get_sistema_id($id_sistema);

echo json_encode($result);

?>