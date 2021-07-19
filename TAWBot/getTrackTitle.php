<?php
$row_number = 1;
$file_out = file("status.txt");

unset($file_out[$row_number]);
file_put_contents("status.txt", implode("", $file_out));
$filename = 'status.txt';
$fh = fopen($filename, 'a') or die("can't open file");

$url = "http://localhost:8000/status-json.xsl";
$json = json_decode(JSON_THROW_ON_ERROR, file_get_contents($url), true);
$title = $json["icestats"]["source"][0]["title"];

$stringData = "$title**";
fwrite($fh, $stringData);
fclose($fh);
?>