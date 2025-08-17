#!/usr/bin/php
<?php
// Print HTTP headers
header("Cache-Control: no-cache");
header("Content-type: text/html");

// Print HTML header
echo "<html><head><title>Environment Variables</title></head>";
echo "<body><h1 align=center>Environment Variables</h1><hr/>";

// Loop through environment variables
foreach ($_SERVER as $key => $value) {
    echo htmlspecialchars($key) . "=" . htmlspecialchars($value) . "<br/>";
}

// Print HTML footer
echo "</body></html>";
?>
