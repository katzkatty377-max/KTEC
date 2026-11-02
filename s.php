<?php
$sales = array(1200, 2500, 1800, 3000, 1500);
$total = 0;

for ($i = 0; $i < count($sales); $i++) {
    $total += $sales[$i];
    
    $commission = $sales[$i] * 0.05;
    
}
$commission = $total * 0.05;
echo "Total sales: " . $total . "\n";
echo "Commission (5%): " . $commission . "\n";

?>