<?php
//Problem 1 — while Loop
$i = 1;

while ($i < 11) {
    echo $i . "\n";
    $i++;
}
?>


<?php
//Problem 2 — do...while Loop
$i = 5;

do {
    echo $i . "\n";
    $i--;
} while ($i > 0);
?>


<?php
//Problem 3 — for Loop
$total = 0;

for ($i = 2; $i <= 20; $i+=2) {
    $total += $i;
}
 echo "Total of even numbers: " . $total;

?>


<?php
//Problem 4 — foreach Loop
$prices = array (150, 250, 100, 300, 200);
$total = 0;

foreach ($prices as $price) {
    echo $price . "\n";
    $total += $price;
} echo "Total price: " . $total;
?>


<?php
//Final challenge — Student Score Analyzer
$scores = array (85, 72, 90, 65, 78);
$total = 0;
$passed = 0;
$i = 0;
$count = 3;

echo "Student scores:" . "\n";

foreach ($scores as $score) {
    echo $score . "\n";
} 

for ($i = 0; $i < count($scores); $i++) {
    $total += $scores[$i];
} 
echo "Total score: ". $total . "\n";

$i = 0;
while ($i < count($scores)) {
    if ($scores[$i] >= 75) {
        $passed++;
    } 
    $i++;
} 
echo "Students passed: " . $passed . "\n";

do {
    echo $count . "\n";
    $count--;
} while ($count >= 1);


?>