<?php
//first problem
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

<?php
//second problem
$i = 0;
$total = 0;

do {
  $i++;
  $total += $i;
  
} while ($i <= 9);

echo "sum: $total";
?>


<?php
//third problem  
$count = 1;  
  
do{  
  echo "Hello Php!" . "\n";  
  $count++;  
} while ($count <= 5);  
  
?>


<?php
//fourth problem
for ($i = 1; $i <= 6; $i++) {
    echo "Programming" . "\n";
}
?>