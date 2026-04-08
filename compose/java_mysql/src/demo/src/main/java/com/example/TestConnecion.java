package com.example; 

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestConnecion {
    public static void main(String[] args) {
        // DATOS DE CONEXIÓN
        // Host: "db" (es el nombre del servicio en docker-compose)
        String url = "jdbc:mysql://db:3306/accesodatos?allowPublicKeyRetrieval=true&useSSL=false";
        String usuario = "root";
        String clave = "root";

        System.out.println("------------------------------------------------");
        System.out.println("INICIANDO TEST DE CONEXIÓN...");
        
        try {
            // Cargar el driver explícitamente (a veces necesario en entornos contenerizados)
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            try (Connection con = DriverManager.getConnection(url, usuario, clave)) {
                System.out.println("ÉXITO: Conexión realizada con la base de datos 'accesodatos'.");
                System.out.println("Usuario: " + usuario);
            }
            
        } catch (ClassNotFoundException e) {
            System.err.println("ERROR: No se encuentra el Driver de MySQL.");
            System.err.println("Asegúrate de que el pom.xml tiene la dependencia cargada.");
        } catch (SQLException e) {
            System.err.println("ERROR DE CONEXIÓN:");
            System.err.println(e.getMessage());
            System.err.println("Revisa si el contenedor 'db' está encendido.");
        }
        System.out.println("------------------------------------------------");
    }
}