#!/usr/bin/php
<?php
// Print HTTP headers
header("Cache-Control: no-cache");
header("Content-type: text/html");

// Print HTML header
echo "<html><head><title>Hello CGI World</title></head>";
echo "<body><h1 align=center>Hello HTML World</h1><hr/>";

// Body content
echo "Hello World<br/>";
echo "This program was generated at: " . date("r") . "<br/>";
echo "Your current IP address is: " . ($_SERVER["REMOTE_ADDR"] ?? "Unknown") . "<br/>";

// Print HTML footer
echo "</body></html>";
?>
