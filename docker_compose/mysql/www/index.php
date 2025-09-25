<?php
$servername = "db";
$username = "alumno";
$password = "alumnopass";
$database = "testdb";

// Conexión MySQL
$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
echo "Conexión exitosa a MySQL desde PHP en Docker!";
?>