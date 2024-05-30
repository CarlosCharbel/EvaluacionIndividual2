<?php

 function conectar(){

$db_host = 'localhost';
$user = "root";
$pass = "rootadmin";
$database = "evaluacion_individual_2";

		$link = new PDO("mysql:host=".$db_host.";dbname=".$database,
						$user,
						$pass,
						array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
		                      PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8")
						);

		return $link;

	}
    
?>