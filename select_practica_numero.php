<?php
require_once "conexion.php";
/* Obtiene elemento de la tabla de productos */

function get_practicas($n_practica){

   date_default_timezone_set('America/Mexico_City');

   $link=conectar();


      $select = "SELECT idalumno,idsistema,numero_practica from practica where numero_practica = " .$n_practica;


   $stmt = $link->prepare($select);
   $stmt -> execute();

   $id = $stmt->fetchAll();

   return $id;

}

/* Main Program */

$n_practica = $_GET['numero'];

$result = get_practicas($n_practica);

echo json_encode($result);

?>