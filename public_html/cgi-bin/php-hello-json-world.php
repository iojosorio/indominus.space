#!/usr/bin/php
<?php
header("Cache-Control: no-cache");
header("Content-type: application/json");

$response = [
    "message" => "Hello World",
    "date" => date("r"),
    "currentIP" => $_SERVER["REMOTE_ADDR"] ?? "Unknown"
];

echo json_encode($response, JSON_PRETTY_PRINT);
?>
