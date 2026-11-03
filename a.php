<?php
$usage = array(120, 95, 150,  80);
$total = 0;
$bill = 0;

echo "Electricity Usage:" . "\n";

foreach ($usage as $usage) {
  echo "$usage kWh" . "\n";

  $total += $usage;
  $cost = $usage * 12;
  $bill += $cost;
}
echo "Total Usage: " . $total . " kWh" . "\n";
echo "Total Bills: ₱" . $bill;
?>