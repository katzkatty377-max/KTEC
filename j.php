<?php
$sales = array(1200, 850, 1500, 950);
$total = 0;
$commissions = 0;

echo "Sales:" . "\n";

foreach ($sales as $sale) {
  echo $sale . "\n";

  $total += $sale;
  $commissions = ($total * 0.05); 
}

echo "Total Sales: " . $total . "\n";
echo "Total Commissions: " . $commissions;


?>