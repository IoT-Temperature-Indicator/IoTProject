<html>
<h1> Ganesh Room Temperature Readings </h1>
<?php

$username="pi";
$password="Charlesdickens12@";
$database="ganesh_temp_holder";
  
mysql_connect(localhost,$username,$password);
@mysql_select_db($database) or die( "Unable to select database");
  
$query="SELECT * FROM tempLog";
$result=mysql_query($query);
  
$num=mysql_numrows($result);
  
// mysql_close();
  
$tempValues = array();
  
$i=0;
// while ($i < $num)
// {
        // $dateAndTemps = array();
        // $datetime = mysql_result($result,$i,"datetime");
        // $temp = mysql_result($result,$i,"temperature");
  
        // $dateAndTemps["Date"] = $datetime;
        // $dateAndTemps["Temp"] = $temp;
  
        // $tempValues[$i]=$dateAndTemps;
        // $i++;
// }
  
// echo json_encode($tempValues);

echo "<table border='1' cellpadding='10'>";
    echo "<tr> <th>Date and Time</th> <th>Temperature</th></tr>";

 while($row = mysql_fetch_array($result))
 {
  echo '<td>' . $row['datetime'] . '</td>';
  echo '<td>' . $row['temperature'] . '</td>';
  echo "</tr>"; 
  }
 echo "</table>";
  
mysql_close();
?>
</html>