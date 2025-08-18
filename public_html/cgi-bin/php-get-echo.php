#!/usr/bin/php
<?php
// Print HTTP headers
header("Cache-Control: no-cache");
header("Content-type: text/html");

// Print HTML header
echo "<html><head><title>GET query string</title></head>";
echo "<body><h1 align=center>GET query string</h1><hr/>";

// Raw query string
$query_string = $_SERVER["QUERY_STRING"] ?? "";
echo "Raw query string: " . htmlspecialchars($query_string) . "<br/><br/>";

// Parse query string into key/value pairs
echo "<table> Formatted Query String:";
foreach ($_GET as $key => $value) {
    echo "<tr><td>" . htmlspecialchars($key) . ":</td><td>" . htmlspecialchars($value) . "</td></tr>";
}
echo "</table>";

// Print HTML footer
echo "</body></html>";
?>
