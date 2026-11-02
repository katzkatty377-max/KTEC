<?php

$correct_password = 1234;

do {
    $password = readline("Enter password uy samuk nis conor: ");
    if ($password != $correct_password) {
        echo "Incorrect password!" . "\n";
    }
} while ($password != $correct_password);
echo "Access granted!";
?>


