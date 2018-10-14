<?php
/*
  Live: http://scotustoons.com/team3/
	Use index.php?id=[idNumber] to look up an events info by id number.
	Use index.php?twitterAccount=[TwitterHandel] to get a list of events a twitter user is signed up to.
	Use index.php (Default, no GET variables.) returns the next event to run.
*/

$db_host = "35.196.238.195"; //Host Address localhost
$db_username = "root"; //MySQL username
$db_pass = "85v6EGGnz8FOmcgD"; //MySQL password
$db_name = "TwitterBot"; //MySQL database*/

////////////////////DO NOT EDIT BELOW THIS LINE///////////////////
$myConnection = mysqli_connect("$db_host","$db_username","$db_pass","$db_name") or die ("could not connect to mysql. " . mysqli_connect_error ($myConnection) );
//$Connection = mysql_connect("$db_host","$db_username","$db_pass","$db_name") or die ("conld not connect to mysql");
//print("connencted");


if(isset($_GET['id'])) {
$sql = "SELECT * FROM events WHERE idNumber=".mysqli_real_escape_string($myConnection, $_GET['id'])." LIMIT 1";
}else if (isset($_GET['twitterAccount'])){
$twitterAccount = mysqli_real_escape_string($myConnection, $_GET['twitterAccount']);
$sql = "SELECT * FROM events WHERE twitterAccount=\"$twitterAccount\"";
}else{$sql = "SELECT * FROM events ORDER BY nextRunTime ASC LIMIT 1";}

//echo $sql . "\n\n";


//Get basic info
$result = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	while($row = mysqli_fetch_array($result)) {
		$id = $row['idNumber'];
		$twitterAccount = $row['twitterAccount'];
		$eventType = $row['eventType'];
		$nextRunTime = $row['nextRunTime'];
		$lastRunTime = $row['lastRunTime'];
		
		echo "$id,$twitterAccount,$eventType,$nextRunTime,$lastRunTime";

//Get special info
		if ($eventType == "localWeather"){
			$result = mysqli_query($myConnection, "SELECT * FROM localWeather WHERE idNumber=$id") or die(mysqli_error($myConnection));
				while($row = mysqli_fetch_array($result)) {
					$location = $row['location'];
					$sendTime = $row['sendTime'];
				}
				echo",$location,$sendTime";
		}else if ($eventType == "dailyStocks"){
			$result = mysqli_query($myConnection, "SELECT * FROM dailyStocks WHERE idNumber=$id") or die(mysqli_error($myConnection));
				while($row = mysqli_fetch_array($result)) {
					$symbol = $row['symbol'];
				}
				echo ",$symbol";
		}
echo "\n";
	}

?>
