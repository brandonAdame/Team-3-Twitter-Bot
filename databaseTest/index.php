<?php
require "connect.php";
header('Content-Type: application/json');

/*
	Use index.php?id=[idNumber] to look up an events info by id number.
	Use index.php?twitterAccount=[TwitterHandel] to get a list of events a twitter user is signed up to.
	Use index.php (Default, no GET variables.) returns the next event to run.
*/




if(isset($_GET['id'])) {
$sql = "SELECT * FROM events WHERE idNumber=".mysqli_real_escape_string($myConnection, $_GET['id'])." LIMIT 1";
}else if (isset($_GET['twitterAccount'])){
$twitterAccount = mysqli_real_escape_string($myConnection, $_GET['twitterAccount']);
$sql = "SELECT * FROM events WHERE twitterAccount=\"$twitterAccount\"";
}else{$sql = "SELECT * FROM events ORDER BY nextRunTime ASC LIMIT 1";}

//echo $sql . "\n\n";

echo "{\"events\":[";
$count = 0;

//Get basic info
$result = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	while($row = mysqli_fetch_array($result)) {
		$id = $row['idNumber'];
		$twitterAccount = $row['twitterAccount'];
		$eventType = $row['eventType'];
		$nextRunTime = $row['nextRunTime'];
		$lastRunTime = $row['lastRunTime'];
		
		if ($count != 0) {echo ",\n";}
		
		echo "{\"id\": \"$id\", \"twitterAccount\": \"$twitterAccount\", \"eventType\": \"$eventType\", \"nextRunTime\": \"$nextRunTime\", \"lastRunTime\":\"$lastRunTime\"";

//Get special info
		if ($eventType == "localWeather"){
			$result = mysqli_query($myConnection, "SELECT * FROM localWeather WHERE idNumber=$id") or die(mysqli_error($myConnection));
				while($row = mysqli_fetch_array($result)) {
					$location = $row['location'];
					$sendTime = $row['sendTime'];
				}
				echo", \"location\": \"$location\", \"sendTime\": \"$sendTime\"";
		}else if ($eventType == "dailyStocks"){
			$result = mysqli_query($myConnection, "SELECT * FROM dailyStocks WHERE idNumber=$id") or die(mysqli_error($myConnection));
				while($row = mysqli_fetch_array($result)) {
					$symbol = $row['symbol'];
				}
				echo ", \"symbol\": \"$symbol\"";
		}
echo "}";
$count = $count + 1;
	}

echo "]}";

?>