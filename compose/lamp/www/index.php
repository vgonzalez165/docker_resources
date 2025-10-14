<?php
$host = "db";          // nombre del servicio en docker-compose
$db   = "testdb";      // base de datos creada en docker-compose
$user = "alumno";      // usuario creado en docker-compose
$pass = "alumnopass";  // contraseña del usuario

try {
    // Crear conexión con PDO
    $dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
    $pdo = new PDO($dsn, $user, $pass);

    // Configurar atributos
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    echo "<h2>Conexión exitosa a MySQL usando PDO</h2>";

    // Crear tabla de prueba si no existe
    $pdo->exec("CREATE TABLE IF NOT EXISTS alumnos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    )");

    // Insertar un registro de prueba
    $stmt = $pdo->prepare("INSERT INTO alumnos (nombre) VALUES (:nombre)");
    $stmt->execute(["nombre" => "Ana"]);

    // Consultar registros
    $stmt = $pdo->query("SELECT * FROM alumnos");
    $alumnos = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo "<h3>Listado de alumnos:</h3>";
    echo "<ul>";
    foreach ($alumnos as $alumno) {
        echo "<li>" . $alumno["id"] . " - " . $alumno["nombre"] . "</li>";
    }
    echo "</ul>";

} catch (PDOException $e) {
    echo "Error de conexión: " . $e->getMessage();
}
?>
