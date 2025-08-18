#!/usr/bin/php
<?php
// Print HTTP headers
header("Cache-Control: no-cache");
header("Content-type: text/html");

// Print HTML header
echo "<html><head><title>General Request Echo</title></head>";
echo "<body><h1 align=center>General Request Echo</h1><hr/>";

// Protocol and Method
$protocol = $_SERVER["SERVER_PROTOCOL"] ?? "Unknown";
$method = $_SERVER["REQUEST_METHOD"] ?? "Unknown";

// Read message body (from stdin)
$body = file_get_contents("php://input", false, null, 0, 1000);

// Print values in a table
echo "<table>";
echo "<tr><td>Protocol:</td><td>" . htmlspecialchars($protocol) . "</td></tr>";
echo "<tr><td>Method:</td><td>" . htmlspecialchars($method) . "</td></tr>";
echo "<tr><td>Message Body:</td><td>" . htmlspecialchars($body) . "</td></tr>";
echo "</table>";

// Print HTML footer
echo "</body></html>";
?>
