#!/usr/bin/php
<?php
session_start();       // Resume session
$_SESSION = [];        // Clear session variables
session_destroy();     // Destroy session
setcookie(session_name(), '', time() - 3600); // Remove session cookie
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Session Destroyed</title>
</head>
<body>
    <h1>Session Destroyed</h1>
    <a href="php-cgiform.html">Back to PHP Form</a><br/>
    <a href="php-sessions-1.php">Back to Page 1</a><br/>
    <a href="php-sessions-2.php">Back to Page 2</a>
</body>
</html>
