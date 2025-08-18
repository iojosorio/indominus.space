#!/usr/bin/php
<?php
header("Cache-Control: no-cache");
header("Content-type: text/html");

echo "<html><head><title>POST Message Body</title></head>";
echo "<body><h1 align=center>POST Message Body</h1><hr/>";

// Read POST body
$body = file_get_contents("php://input");
echo "Message Body: " . htmlspecialchars($body) . "<br/>";

echo "</body></html>";
?>
