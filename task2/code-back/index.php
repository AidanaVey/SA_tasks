<?php

$path = explode('/', $_SERVER['REQUEST_URI']);

$function = $path[1];
$arg = $path[2];

echo json_encode($function($arg));

function getColor(string $subject) {
    if ($subject == 'petal') {
        return 'green';
    }
    if ($subject == 'water') {
        return 'blue';
    }
    else {
        return 'unknown';
    }
}